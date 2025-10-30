import pytest
import json
import os
from datetime import datetime
from unittest.mock import patch, mock_open
from history import History


class TestHistoryBasics:
    """Test basic History functionality"""

    def test_init_with_default_max_entries(self):
        """Test History initialization with default max entries"""
        history = History()
        assert history.max_entries == 100
        assert len(history.history) == 0

    def test_init_with_custom_max_entries(self):
        """Test History initialization with custom max entries"""
        history = History(max_entries=50)
        assert history.max_entries == 50
        assert len(history.history) == 0


class TestAddEntry:
    """Test add_entry functionality"""

    def test_add_single_entry(self):
        """Test adding a single entry to history"""
        history = History()
        history.add_entry('+', [2, 3], 5.0, 'basic')
        
        assert len(history.history) == 1
        entry = history.history[0]
        assert entry['operation'] == '+'
        assert entry['operands'] == [2, 3]
        assert entry['result'] == 5.0
        assert entry['mode'] == 'basic'
        assert 'timestamp' in entry

    def test_add_entry_with_default_mode(self):
        """Test adding entry with default mode"""
        history = History()
        history.add_entry('*', [4, 5], 20.0)
        
        entry = history.history[0]
        assert entry['mode'] == 'basic'

    def test_add_entry_timestamp_format(self):
        """Test that timestamp is in ISO format"""
        history = History()
        with patch('history.datetime') as mock_datetime:
            mock_datetime.now.return_value.isoformat.return_value = '2023-01-01T12:00:00'
            history.add_entry('+', [1, 1], 2.0)
            
            entry = history.history[0]
            assert entry['timestamp'] == '2023-01-01T12:00:00'

    def test_add_entry_exceeds_max_entries(self):
        """Test that old entries are removed when max_entries is exceeded"""
        history = History(max_entries=2)
        
        # Add 3 entries
        history.add_entry('+', [1, 2], 3.0)
        history.add_entry('-', [5, 2], 3.0)
        history.add_entry('*', [2, 3], 6.0)
        
        # Should only have 2 entries, oldest should be removed
        assert len(history.history) == 2
        assert history.history[0]['operation'] == '-'
        assert history.history[1]['operation'] == '*'


class TestGetRecentEntries:
    """Test get_recent_entries functionality"""

    def test_get_recent_entries_default_count(self):
        """Test getting recent entries with default count"""
        history = History()
        for i in range(10):
            history.add_entry('+', [i, 1], i + 1)
        
        recent = history.get_recent_entries()
        assert len(recent) == 5  # default count
        assert recent[-1]['result'] == 10  # last entry

    def test_get_recent_entries_custom_count(self):
        """Test getting recent entries with custom count"""
        history = History()
        for i in range(10):
            history.add_entry('+', [i, 1], i + 1)
        
        recent = history.get_recent_entries(3)
        assert len(recent) == 3
        assert recent[-1]['result'] == 10  # last entry

    def test_get_recent_entries_more_than_available(self):
        """Test getting more recent entries than available"""
        history = History()
        history.add_entry('+', [1, 2], 3.0)
        history.add_entry('-', [5, 2], 3.0)
        
        recent = history.get_recent_entries(10)
        assert len(recent) == 2  # all available entries

    def test_get_recent_entries_empty_history(self):
        """Test getting recent entries from empty history"""
        history = History()
        recent = history.get_recent_entries()
        assert len(recent) == 0


class TestSearchOperations:
    """Test search_operations functionality"""

    def test_search_operations_exact_match(self):
        """Test searching for exact operation match"""
        history = History()
        history.add_entry('+', [1, 2], 3.0)
        history.add_entry('-', [5, 2], 3.0)
        history.add_entry('+', [3, 4], 7.0)
        
        results = history.search_operations('+')
        assert len(results) == 2
        assert all('+' in entry['operation'] for entry in results)

    def test_search_operations_partial_match(self):
        """Test searching for partial operation match"""
        history = History()
        history.add_entry('sin', [30], 0.5)
        history.add_entry('cos', [60], 0.5)
        history.add_entry('tan', [45], 1.0)
        
        results = history.search_operations('sin')
        assert len(results) == 1
        assert results[0]['operation'] == 'sin'

    def test_search_operations_no_match(self):
        """Test searching for non-existent operation"""
        history = History()
        history.add_entry('+', [1, 2], 3.0)
        
        results = history.search_operations('sqrt')
        assert len(results) == 0


class TestClearHistory:
    """Test clear_history functionality"""

    def test_clear_history_removes_all_entries(self):
        """Test that clear_history removes all entries"""
        history = History()
        for i in range(5):
            history.add_entry('+', [i, 1], i + 1)
        
        assert len(history.history) == 5
        history.clear_history()
        assert len(history.history) == 0


class TestGetStatistics:
    """Test get_statistics functionality"""

    def test_get_statistics_empty_history(self):
        """Test statistics for empty history"""
        history = History()
        stats = history.get_statistics()
        assert stats == {}

    def test_get_statistics_no_numeric_results(self):
        """Test statistics when no numeric results exist"""
        history = History()
        # Add entry with non-numeric result
        history.add_entry('bin', [10], 'invalid_result')
        history.history[0]['result'] = 'string_result'  # Force non-numeric
        
        stats = history.get_statistics()
        assert stats == {}

    def test_get_statistics_with_valid_data(self):
        """Test statistics calculation with valid data"""
        history = History()
        history.add_entry('+', [1, 2], 3.0)
        history.add_entry('*', [2, 5], 10.0)
        history.add_entry('+', [3, 4], 7.0)
        history.add_entry('-', [10, 3], 7.0)
        
        stats = history.get_statistics()
        
        assert stats['total_calculations'] == 4
        assert stats['average_result'] == 6.75  # (3+10+7+7)/4
        assert stats['min_result'] == 3.0
        assert stats['max_result'] == 10.0
        assert stats['most_used_operation'] == '+'  # appears twice


class TestExportImportHistory:
    """Test export_history and import_history functionality"""

    def test_export_history(self):
        """Test exporting history to JSON file"""
        history = History()
        history.add_entry('+', [1, 2], 3.0)
        history.add_entry('-', [5, 2], 3.0)
        
        mock_file = mock_open()
        with patch('builtins.open', mock_file):
            history.export_history('test.json')
            
        mock_file.assert_called_once_with('test.json', 'w')
        # Verify json.dump was called with correct data
        written_data = ''.join(call.args[0] for call in mock_file().write.call_args_list)
        imported_data = json.loads(written_data)
        assert len(imported_data) == 2
        assert imported_data[0]['operation'] == '+'

    def test_import_history(self):
        """Test importing history from JSON file"""
        history = History()
        test_data = [
            {'operation': '+', 'operands': [1, 2], 'result': 3.0, 'mode': 'basic', 'timestamp': '2023-01-01T12:00:00'},
            {'operation': '*', 'operands': [3, 4], 'result': 12.0, 'mode': 'basic', 'timestamp': '2023-01-01T12:01:00'}
        ]
        
        mock_file = mock_open(read_data=json.dumps(test_data))
        with patch('builtins.open', mock_file):
            history.import_history('test.json')
            
        mock_file.assert_called_once_with('test.json', 'r')
        assert len(history.history) == 2
        assert history.history[0]['operation'] == '+'
        assert history.history[1]['operation'] == '*'

    def test_import_history_overwrites_existing(self):
        """Test that import overwrites existing history"""
        history = History()
        # Add some existing data
        history.add_entry('-', [10, 5], 5.0)
        
        test_data = [
            {'operation': '+', 'operands': [1, 2], 'result': 3.0, 'mode': 'basic', 'timestamp': '2023-01-01T12:00:00'}
        ]
        
        mock_file = mock_open(read_data=json.dumps(test_data))
        with patch('builtins.open', mock_file):
            history.import_history('test.json')
            
        # Should only have imported data, existing data should be gone
        assert len(history.history) == 1
        assert history.history[0]['operation'] == '+'
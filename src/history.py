from typing import List, Dict, Any
from datetime import datetime
import json

class History:
    def __init__(self, max_entries: int = 100):
        self.history: List[Dict[str, Any]] = []
        self.max_entries = max_entries
    
    def add_entry(self, operation: str, operands: List, result: float, mode: str = "basic"):
        """Add a calculation to history"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'operation': operation,
            'operands': operands,
            'result': result,
            'mode': mode
        }
        
        self.history.append(entry)
        
        if len(self.history) > self.max_entries:
            self.history.pop(0)
    
    def get_recent_entries(self, count: int = 5) -> List[Dict[str, Any]]:
        """Get recent calculation entries"""
        return self.history[-count:] if count <= len(self.history) else self.history
    
    def search_operations(self, operation: str) -> List[Dict[str, Any]]:
        """Search history by operation type"""
        return [entry for entry in self.history if operation in entry['operation']]
    
    def clear_history(self):
        """Clear all history"""
        self.history.clear()
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get calculation statistics"""
        if not self.history:
            return {}
        
        results = [entry['result'] for entry in self.history if isinstance(entry['result'], (int, float))]
        
        if not results:
            return {}
        
        return {
            'total_calculations': len(self.history),
            'average_result': sum(results) / len(results),
            'min_result': min(results),
            'max_result': max(results),
            'most_used_operation': max(
                set(entry['operation'] for entry in self.history),
                key=list(entry['operation'] for entry in self.history).count
            )
        }
    
    def export_history(self, filename: str):
        """Export history to JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.history, f, indent=2)
    
    def import_history(self, filename: str):
        """Import history from JSON file"""
        with open(filename, 'r') as f:
            self.history = json.load(f)
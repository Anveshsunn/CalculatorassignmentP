import json
import os
from collections import deque

class HistoryManager:
    """Class responsible for managing history of calculations, including save/load and undo/redo."""
    
    def __init__(self, config):
        self.config = config
        self.history = deque(maxlen=self.config.max_history_count)
        self.undo_stack = []
        self.redo_stack = []

    def _log_history(self, entry):
        """Log each operation to history."""
        self.history.append(entry)
        if self.config.auto_save_history:
            self.save_history()

    def save_history(self):
        """Save history to a JSON file."""
        if not os.path.exists(self.config.history_dir):
            os.makedirs(self.config.history_dir)
        
        history_file = os.path.join(self.config.history_dir, 'history.json')
        with open(history_file, 'w', encoding=self.config.file_encoding) as file:
            json.dump(list(self.history), file)

    def load_history(self):
        """Load history from a JSON file."""
        history_file = os.path.join(self.config.history_dir, 'history.json')
        if os.path.exists(history_file):
            with open(history_file, 'r', encoding=self.config.file_encoding) as file:
                self.history = deque(json.load(file), maxlen=self.config.max_history_count)

    def clear_history(self):
        """Clear the entire calculation history."""
        self.history.clear()
        self.save_history()

    def undo(self):
        """Undo the last operation."""
        if self.history:
            entry = self.history.pop()
            self.undo_stack.append(entry)
            self.save_history()
            return entry

    def redo(self):
        """Redo the previously undone operation."""
        if self.undo_stack:
            entry = self.undo_stack.pop()
            self.history.append(entry)
            self.save_history()
            return entry

    def get_history(self):
        """Return the full list of history entries."""
        return list(self.history)

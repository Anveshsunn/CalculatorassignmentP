# src/history_manager.py

import os
import json
from .config import CalculatorConfig

class HistoryManager:
    def __init__(self):
        self.history = []
        self.file_path = os.path.join(CalculatorConfig.BASE_DIR, "calc_history.json")

    def add_to_history(self, operation, result):
        self.history.append({"operation": operation, "result": result})
        if CalculatorConfig.AUTO_SAVE:
            self.save_history()

    def save_history(self):
        with open(self.file_path, "w", encoding=CalculatorConfig.DEFAULT_ENCODING) as f:
            json.dump(self.history[-CalculatorConfig.MAX_HISTORY_SIZE:], f)

    def load_history(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding=CalculatorConfig.DEFAULT_ENCODING) as f:
                self.history = json.load(f)

    def clear_history(self):
        self.history = []

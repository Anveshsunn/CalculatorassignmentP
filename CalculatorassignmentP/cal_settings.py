import os

class Config:
    def __init__(self):
        # Directory where history will be stored
        self.history_dir = os.getenv("CALCULATOR_HISTORY_DIR", "/tmp/calculator")
        
        # Max number of operations to store in history
        self.max_history_count = int(os.getenv("CALCULATOR_HISTORY_SIZE", 50))
        
        # Should history auto-save after each operation
        self.auto_save_history = os.getenv("CALCULATOR_AUTO_SAVE_HISTORY", "true").lower() == "true"
        
        # Precision of decimal results
        self.result_precision = int(os.getenv("CALCULATOR_RESULT_PRECISION", 5))
        
        # Maximum allowed value for inputs
        self.max_input_value = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1e100))
        
        # File encoding for saving/loading history
        self.file_encoding = os.getenv("CALCULATOR_FILE_ENCODING", "utf-8")

    def __repr__(self):
        return (f"Config(history_dir={self.history_dir}, max_history_count={self.max_history_count}, "
                f"auto_save_history={self.auto_save_history}, result_precision={self.result_precision}, "
                f"max_input_value={self.max_input_value}, file_encoding={self.file_encoding})")

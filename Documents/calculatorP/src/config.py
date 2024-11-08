# src/config.py

import os

class CalculatorConfig:
    BASE_DIR = os.getenv("CALCULATOR_BASE_DIR", "./")
    MAX_HISTORY_SIZE = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100"))
    AUTO_SAVE = os.getenv("CALCULATOR_AUTO_SAVE", "true") == "true"
    PRECISION = int(os.getenv("CALCULATOR_PRECISION", "10"))
    MAX_INPUT_VALUE = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1e100"))
    DEFAULT_ENCODING = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")

# main.py

from src.calculator import Calculator
from src.history_manager import HistoryManager

def main():
    calculator = Calculator()
    history_manager = HistoryManager()

    print("Welcome to the calculator. Type 'exit' to quit.")
    while True:
        command = input("Enter command: ")

        if command.lower() == "exit":
            print("Exiting calculator.")
            break

        elif command.lower() == "add":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calculator.add(a, b)
            print(f"The result is: {result}")
            history_manager.add_to_history(f"add {a} and {b}", result)

        elif command.lower() == "subtract":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calculator.subtract(a, b)
            print(f"The result is: {result}")
            history_manager.add_to_history(f"subtract {a} and {b}", result)

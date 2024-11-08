from cal_settings import Config
from calculator_logic import Calculator

def main():
    # Load configuration
    config = Config()
    calculator = Calculator(config)

    print("Welcome to the Smart Python Calculator!")
    print("Available operations: add, subtract, multiply, divide, power, sqrt")
    print("Type 'exit' to quit, 'history' to see previous calculations.")

    while True:
        try:
            # Get user input for the operation
            operation = input("\nEnter operation (add, subtract, multiply, divide, power, sqrt): ").strip()

            # Exit condition
            if operation == "exit":
                print("Exiting the calculator. Goodbye!")
                break  # Exit the loop

            # History command to display past calculations
            elif operation == "history":
                history = calculator.get_history()
                if not history:
                    print("No history available.")
                else:
                    print("Calculation History:")
                    for entry in history:
                        print(entry)

            # Clear history command
            elif operation == "clear":
                calculator.clear_history()
                print("History cleared.")

            # Undo last operation
            elif operation == "undo":
                undone = calculator.undo()
                if undone:
                    print(f"Undone: {undone}")
                else:
                    print("Nothing to undo.")

            # Redo last undone operation
            elif operation == "redo":
                redone = calculator.redo()
                if redone:
                    print(f"Redone: {redone}")
                else:
                    print("Nothing to redo.")

            else:
                # For other operations, get the operands from user
                operands = input("Enter operands (comma-separated): ").strip()
                operands = [float(x) for x in operands.split(",")]

                # Perform the operation based on input
                if operation == "add":
                    print(f"Result: {calculator.add(*operands)}")
                elif operation == "subtract":
                    print(f"Result: {calculator.subtract(*operands)}")
                elif operation == "multiply":
                    print(f"Result: {calculator.multiply(*operands)}")
                elif operation == "divide":
                    print(f"Result: {calculator.divide(*operands)}")
                elif operation == "power":
                    print(f"Result: {calculator.power(*operands)}")
                elif operation == "sqrt":
                    if len(operands) != 1:
                        print("Error: Square root operation requires only one operand.")
                    else:
                        print(f"Result: {calculator.sqrt(operands[0])}")
                else:
                    print(f"Unknown operation: {operation}")

        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("Enter 'exit' to quit")
    # You can add code here to take input and use the functions

    while True:
        operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
        
        if operation == 'exit':
            break
        
        if operation in ['add', 'subtract', 'multiply', 'divide']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue
            
            if operation == 'add':
                print(f"Result: {addition(num1, num2)}")
            elif operation == 'subtract':
                print(f"Result: {subtraction(num1, num2)}")
            elif operation == 'multiply':
                print(f"Result: {multiplication(num1, num2)}")
            elif operation == 'divide':
                print(f"Result: {division(num1, num2)}")
        else:
            print("Invalid operation. Please try again.")
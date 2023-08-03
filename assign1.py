def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    addition_result = add_numbers(num1, num2)
    subtraction_result = subtract_numbers(num1, num2)
    multiplication_result = multiply_numbers(num1, num2)

    print(f"Addition Result: {addition_result}")
    print(f"Subtraction Result: {subtraction_result}")
    print(f"Multiplication Result: {multiplication_result}")

# calc function
def calculate(num1, num2, operator):
    if operator == 1:
        result = num1 + num2
    elif operator == 2:
        result = num1 - num2
    elif operator == 3:
        result = num1 * num2
    elif operator == 4:
        if num2 != 0:  # check for division by zero
            result = num1 / num2
        else:
            return "error: division by zero!"
    else:
        return "error: invalid operation!"

    # Truncate the result
    if result.is_integer():
        return int(result)
    else:
        return round(result, 2)

# verification of number input


def is_valid_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


while True:
    num1 = input("Input first number: ")
    while not is_valid_number(num1):
        num1 = input("Input first VALID number: ")

    num2 = input("Input second number: ")
    while not is_valid_number(num2):
        num2 = input("nput second VALID number: ")

    # Output menu of operations
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Getting an operation selection from the user
    choice = input("Enter your choice (1-4): ")
    while choice not in ['1', '2', '3', '4']:
        choice = input("Enter your choice (1-4): ")

    num1 = float(num1)
    num2 = float(num2)
    choice = int(choice)

    # Calling the calculate function and outputting the result
    result = calculate(num1, num2, choice)
    print("Result:", result)

    # Checking if the user wants to continue
    restart = input("Do you want to continue? (y or n): ")
    if restart.lower() != 'y':
        break

# calc function

def calculate(num1, num2, operator):
    if operator == 1:
        return num1 + num2
    elif operator == 2:
        return num1 - num2
    elif operator == 3:
        return num1 * num2
    elif operator == 4:
        if num2 != 0:  
            return num1 / num2
        else:
            return "error: division by zero!"
    else:
        return "Invalid operation"


num1 = int(input("input first number: "))
num2 = int(input("input second number: "))

print("Please select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


choice = int(input("Enter your choice (1-4): "))


result = calculate(num1, num2, choice)
print("Result:", result)
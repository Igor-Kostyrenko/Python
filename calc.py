# calc function

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  
            return num1 / num2
        else:
            return "error: division by zero!"
    else:
        return "Invalid operation"


num1 = int(input("input first number: "))
num2 = int(input("input second number: "))
operator = input("input operator (+, -, *, /): ")


result = calculate(num1, num2, operator)
print("Result:", result)
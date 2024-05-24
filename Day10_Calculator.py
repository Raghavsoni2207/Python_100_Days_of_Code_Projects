logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# Add
def add(num1, num2):
    return num1+num2

# Subtract
def subtract(num1, num2):
    return num1-num2

# Multiply
def multiply(num1, num2):
    return num1*num2

# Divide
def divide(num1, num2):
    return num1/num2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(logo)
    
    number_1 = float(input("What's the first number: "))
    for key in operations:
        print(key)

    status = True

    while status:
        operation_symbol = input("Pick an operator : ")
        number_2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(number_1, number_2)

        print(f"{number_1} {operation_symbol} {number_2} = {answer}")

        status_input = input(f"Type 'y' to continue calculating with {answer}, type 'c' to start a new calculation, or type 'n' to exit: ").lower()

        if status_input == 'y':
            number_1 = answer
        elif status_input == 'c':
            calculator()
        else:
            status = False

calculator()

# Basic Calculator

# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division

# 1.

def Addition(input_1, input_2):
    sum = input_1 + input_2
    return sum

# 2.

def Subtraction(input_1, input_2):
    difference = input_1 - input_2
    return difference

# 3.

def Multiplication(input_1, input_2):
    product = input_1 * input_2
    return product

# 4.

def Division(input_1, input_2):
    division = input_1 / input_2
    return division

while True:
    choice_of_operation_question = input("""
    Please pick one of the options.

    Select 1 for Addition
    Select 2 for Subtraction
    Select 3 for Multiplication
    Select 4 for Division

    """)
    
    if choice_of_operation_question in ('1', '2', '3', '4'):
        num_1 = float(input("Enter the first value: "))
        num_2 = float(input("Enter the second value: "))

        if choice_of_operation_question == '1':
            print("Addition")
            print("-" * 50)
            print(num_1, "+", num_2, "=", Addition(num_1, num_2))

        elif choice_of_operation_question == '2':
            print("Subtraction")
            print("-" * 50)
            print(num_1, "-", num_2, "=", Subtraction(num_1, num_2))

        elif choice_of_operation_question == '3':
            print("Multiplication")
            print("-" * 50)
            print(num_1, "*", num_2, "=", Multiplication(num_1, num_2))

        elif choice_of_operation_question == '4':
            print("Division")         
            print("-" * 50)
            print(num_1, "/", num_2, "=", Division(num_1, num_2))
        
        break

    else:
        print("Invalid entry.")
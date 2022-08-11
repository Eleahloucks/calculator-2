"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)


while True:

    equation_input = input("Enter your equation>")
    tokens = equation_input.split(' ')

    # if "q" in tokens:
    #     print("You will exit.")
    #     break

    # elif len(tokens) < 2:
    #     print("Not enough inputs.")
    #     continue

    # operator = tokens[0]
    # num1 = tokens[1]

    # if len(tokens) < 3:
    #     num2 = "0"

    # else:
    #     num2 = tokens[2]

    # if len(tokens) > 3:
    #     num3 = tokens[3]


    if tokens[0] == 'q':
        print("You've exited.")
        break
    elif tokens[0] == '+':
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        print(add(num1,num2))
    elif tokens[0] == '-':
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        print(subtract(num1,num2))
    elif tokens[0] == '*':
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        print(multiply(num1,num2))
    elif tokens[0] == '/':
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        print(divide(num1,num2))
    elif tokens[0] == 'square':
        num1 = float(tokens[1])
        print(square(num1))
    elif tokens[0] == 'cube':
        num1 = float(tokens[1])
        print(cube(num1))
    elif tokens[0] == 'pow':
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        print(power(num1,num2))
    elif tokens[0] == 'mod':
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        print(mod(num1,num2))
    else:
        print('Please enter equation in correct format.')





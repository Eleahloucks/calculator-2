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

equation_input = input("Enter your equation>")
tokens = equation_input.split(' ')

while True:
    if tokens[0] == 'q':
        print("You've exited.")
        break
    else:
        if tokens[0] == 'pow':
          power(tokens[1],tokens[2])


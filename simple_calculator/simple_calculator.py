#! /usr/bin/python
# **************************************************************************** #
#                                                                              #
#   -- simple_calculator.py --                                  /`·.¸          #
#                                                              /¸...¸`:·       #
#   By: ines_lemos                                         ¸.·´  ¸   `·.¸.·´)  #
#   Github: github.com/vapreace                           : © ):´;      ¸  {   #
#   Linkedin: https://www.linkedin.com/in/ines-s-lemos/    `·.¸ `·  ¸.·´\`·¸)  #
#   Last updated: 2024-08-09                                   `\\´´\¸.·´      #
#                                                                              #
# **************************************************************************** #

"""
This script provides a simple calculator that can perform basic arithmetic operations:
addition, subtraction, multiplication, and division. The user can choose an operation
and input two numbers to get the result. The script continues to prompt the user for
operations until they choose to exit.
"""


def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

operations = {
    'a': add,
    's': subtract,
    'm': multiply,
    'd': divide
}

operators = {
    'a': '+',
	's': '-',
	'm': '*',
	'd': '/'
}

print("""
╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗                    
║║║║╣ ║  ║  ║ ║║║║║╣    ║ ║ ║                    
╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝   ╩ ╚═╝                    
╔═╗╦╔╦╗╔═╗╦  ╔═╗  ╔═╗╔═╗╦  ╔═╗╦ ╦╦  ╔═╗╔╦╗╔═╗╦═╗┬
╚═╗║║║║╠═╝║  ║╣   ║  ╠═╣║  ║  ║ ║║  ╠═╣ ║ ║ ║╠╦╝│
╚═╝╩╩ ╩╩  ╩═╝╚═╝  ╚═╝╩ ╩╩═╝╚═╝╚═╝╩═╝╩ ╩ ╩ ╚═╝╩╚═o
""")

while True:
	print("What operation would you like to perform?")
	print("(a)dd")
	print("(s)ubtract")
	print("(m)ultiply")
	print("(d)ivide")
	operation = input("Enter choice (a/s/m/d): ").strip().lower()
 
	if operation not in operations:
		print("Invalid operation! Please choose a valid operation.\n")
		continue

	try:
		x = float(input("Enter the first number: "))
		y = float(input("Enter the second number: "))
		result = operations[operation](x, y)
		print(f"{x} {operators[operation]} {y} = {result}\n")
	except ZeroDivisionError:
		print("Cannot divide by zero!\n")
	except ValueError:
		print("Invalid input. Please enter numeric values.\n")

	repeat = input("Would you like to perform another operation? (y to continue): ").strip().lower()
	if repeat != 'y':
		print("See you later!")
		break
	print()
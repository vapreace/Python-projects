#! /usr/bin/python
# **************************************************************************** #
#                                                                              #
#   -- countdown_timer.py --                                    /`·.¸          #
#                                                              /¸...¸`:·       #
#   By: ines_lemos                                         ¸.·´  ¸   `·.¸.·´)  #
#   Github: github.com/vapreace                           : © ):´;      ¸  {   #
#   Linkedin: https://www.linkedin.com/in/ines-s-lemos/    `·.¸ `·  ¸.·´\`·¸)  #
#   Last updated: 2024-08-09                                   `\\´´\¸.·´      #
#                                                                              #
# **************************************************************************** #

import time

def countdown(mins, secs):
	"""
	Executes a countdown timer for a specified duration in minutes and seconds.

	Args:
		mins (int): The number of minutes for the countdown.
		secs (int): The number of seconds to add to the minutes for the countdown.

	The function updates the timer display every second until it reaches 0:00, then prints 'Time is up!'.
	"""
	while mins > 0 or secs > 0:
		timeformat = '{:02d}:{:02d}'.format(mins, secs) # format the time as mm:ss with leading zeros
		print(timeformat, end='\r') # print the time on the same line each time
		time.sleep(1) # wait for 1 second
		if secs == 0: # if seconds reach 0, decrement minutes and reset seconds to 59
			mins -= 1
			secs = 59
		else: # otherwise, just decrement seconds
			secs -= 1
	print('Time is up!')

def valid_input(prompt):
	"""
	Prompts the user for a positive integer input, validating the input.

	Args:
		prompt (str): The message displayed to the user.

	Returns:
		int: A positive integer input by the user.

	The function repeatedly prompts the user until a valid positive integer is entered.
	"""
	while True:
		try:
			value = int(input(prompt)) # get user input for minutes and seconds
			if value < 0: # check if the input is negative
				raise ValueError
			return value
		except ValueError: # handle invalid input
			print("Please enter a valid number")

# Print a countdown timer ASCII art
print('''
+8-=-=-=-=-=-8+  
 | ,.-'"'-., |   
 |/         \|   
 |\:.     .:/|    _____                   _      _                     
 | \:::::::/ |   /  __ \                 | |    | |                    
 |  \:::::/  |   | /  \/ ___  _   _ _ __ | |_ __| | _____      ___ __  
 |   \:::/   |   | |    / _ \| | | | '_ \| __/ _` |/ _ \ \ /\ / / '_ \ 
 |    ):(    |   | \__/\ (_) | |_| | | | | || (_| | (_) \ V  V /| | | |
 |   / . \   |    \____/\___/ \__,_|_| |_|\__\__,_|\___/ \_/\_/ |_| |_|
 |  /  .  \  |    _   _
 | /   .   \ |   | | (_)                                               
 |/   .:.   \|   | |_ _ _ __ ___   ___ _ __                            
 |\.:::::::./|   | __| | '_ ` _ \ / _ \ '__|                           
 | '--___--' |   | |_| | | | | | |  __/ |                              
+8-=-=-=-=-=-8+   \__|_|_| |_| |_|\___|_|                              
''')

# Get the number of minutes and seconds from the user
minutes = valid_input('Enter the number of minutes: ')
seconds = valid_input('Enter the number of seconds: ')

# Start the countdown timer
countdown(minutes, seconds)
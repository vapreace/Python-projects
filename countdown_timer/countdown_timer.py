import time
import ascii_art

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

print(ascii_art.ascii_letters[0]) # print the title of the countdown timer

# Get the number of minutes and seconds from the user
minutes = valid_input('Enter the number of minutes: ')
seconds = valid_input('Enter the number of seconds: ')

# Start the countdown timer
countdown(minutes, seconds)
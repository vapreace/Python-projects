import random
import string
import ascii_art

def validate_password_length():
	"""
	Prompts the user to enter a desired password length and validates it.

	The function ensures the password length is between 8 and 20 characters.
	If the input is not within this range or is not a number, it prompts the user again until a valid input is provided.

	Returns:
		int: The validated password length.
	"""
	while True:
		try:
			length = int(input("Enter the length of the password.\nTo ensure security, it should be between 8 and 20 characters: "))
			if length < 8 or length > 20:
				raise ValueError
			return length
		except ValueError:
			print("Invalid input.\n")

def validate_input(prompt):
	"""
	Prompts the user with a question and expects a 'y' or 'n' response.

	Args:
		prompt (str): The question to prompt the user with.

	Returns:
		bool: True if the user responds with 'y', False if the user responds with 'n'.

	The function ensures that the response is either 'y' or 'n'.
	If the input is invalid, it prompts the user again until a valid input is provided.
	"""
	while True:
		response = input(prompt).strip().lower() # Remove leading/trailing whitespace and convert to lowercase
		if response.lower() == "y":
			return True
		elif response.lower() == "n":
			return False
		else:
			print("Please enter 'y' or 'n'.")

def generate_password(length, digits, lowercase, uppercase, symbols):
	"""
	Generates a password based on user preferences.

	Args:
		length (int): The length of the password.
		digits (bool): Whether to include digits in the password.
		lowercase (bool): Whether to include lowercase letters in the password.
		uppercase (bool): Whether to include uppercase letters in the password.
		symbols (bool): Whether to include symbols in the password.

	The function ensures that at least one character from each selected category is included in the password.
	The remaining characters are filled randomly from the selected categories, and the final password is shuffled to randomize the character order.
	"""

	generate_another = True

	while generate_another:
		password = []
		possible_characters = ""
  
		if digits:
			possible_characters += string.digits # Add digits to the possible characters
			password.append(random.choice(string.digits)) # Add a random digit to the password to ensure at least one digit is included
   
		if lowercase:
			possible_characters += string.ascii_lowercase
			password.append(random.choice(string.ascii_lowercase))
   
		if uppercase:
			possible_characters += string.ascii_uppercase
			password.append(random.choice(string.ascii_uppercase))
   
		if symbols:
			possible_characters += string.punctuation
			password.append(random.choice(string.punctuation))
   
		if not possible_characters:
			print("No characters selected. Exiting program. Bye!")
			return

		while len(password) < length:
			password.append(random.choice(possible_characters))
   
		random.shuffle(password) # Shuffle the password to randomize the order of characters
		print("\nGenerated password:", "".join(password)) # Join the password list into a string with no separator
		generate_another = validate_input("Generate another password? (y/n): ") # Ask the user if they want to generate another password or exit
	print("Exiting program. Bye!")


def main():
	"""
	The main function that runs the password generator program.
	"""
	print(ascii_art.ascii_title[0])
	length = validate_password_length()
	digits = validate_input("Include digits? (y/n): ")
	lowercase = validate_input("Include lowercase letters? (y/n): ")
	uppercase = validate_input("Include uppercase letters? (y/n): ")
	symbols = validate_input("Include symbols? (y/n): ")
	generate_password(length, digits, lowercase, uppercase, symbols)

main()
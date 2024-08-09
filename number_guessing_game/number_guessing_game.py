#! /usr/bin/python
# **************************************************************************** #
#                                                                              #
#   -- number_guessing_game.py --                               /`·.¸          #
#                                                              /¸...¸`:·       #
#   By: ines_lemos                                         ¸.·´  ¸   `·.¸.·´)  #
#   Github: github.com/vapreace                           : © ):´;      ¸  {   #
#   Linkedin: https://www.linkedin.com/in/ines-s-lemos/    `·.¸ `·  ¸.·´\`·¸)  #
#   Last updated: 2024-08-09                                   `\\´´\¸.·´      #
#                                                                              #
# **************************************************************************** #

# Print the game title and rules
print("""
.-. .-..-. .-..-.   .-..----. .----..----.
|  `| || { } ||  `.'  || {}  }| {_  | {}  }
| |\  || {_} || |\ /| || {}  }| {__ | .-. \\
`-' `-'`-----'`-' ` `-'`----' `----'`-' `-'
 .---. .-. .-..----. .----. .----..-..-. .-. .---.
/   __}| { } || {_  { {__  { {__  | ||  `| |/   __}
\  {_ }| {_} || {__ .-._} }.-._} }| || |\  |\  {_ }
 `---' `-----'`----'`----' `----' `-'`-' `-' `---'
 .---.   .--.  .-.   .-..----.
/   __} / {} \ |  `.'  || {_  
\  {_ }/  /\  \| |\ /| || {__ 
 `---' `-'  `-'`-' ` `-'`----'
""")

print("""
+----------------------------------------------------------+
| Welcome to the Number Guessing Game!                     |
|                                                          |
| Rules:                                                   |
| --> Think of a number between 0 and 1000                 |
| --> I will try to guess the number you're thinking of in |
|     10 attempts.                                         |
| --> After each guess, tell me if I'm correct, or if your |
|     number is higher or lower than my guess.             |
| Let's begin!                                             |
+----------------------------------------------------------+
""")

# Start the game
print("Time to choose a number! Can we continue? (Click ENTER when you are ready)")
input()

# Reset function to start the game again
def reset():
    return 0, 1000, 1

min, max, count = reset()

# Main loop of the game
while True:
    # Check if the user is cheating
    if max < min:
        print("It looks like you are cheating... Let's try again!")
        min, max, count = reset()
        continue
    
    # Guess the number
    attempt = (max + min) // 2
    
    # Print the guess and ask for feedback
    print(f"\nIs it {attempt}? Attempt number {count}")
    print("y - yes!\nl - lower!\nh - higher!")
    ans = input().strip().lower()
    
    # Check the user's feedback
    if ans == "y":
        break
    elif ans == "l":
        max = attempt - 1
        count += 1
    elif ans == "h":
        min = attempt + 1
        count += 1
    else:
        print("Wrong input! Let's try one more time.")
        continue
    
# Print the result - END OF THE GAME
print(f"\nOh yes! I got it right in {count} attempts. :)")
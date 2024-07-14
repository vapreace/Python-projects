# Game presented in ASCII art
ascii_art = [
    ".-. .-..-. .-..-.   .-..----. .----..----.     .---. .-. .-..----. .----. .----..-..-. .-. .---.     .---.   .--.  .-.   .-..----.\n"
    "|  `| || { } ||  `.'  || {}  }| {_  | {}  }   /   __}| { } || {_  { {__  { {__  | ||  `| |/   __}   /   __} / {} \ |  `.'  || {_  \n"
    "| |\  || {_} || |\ /| || {}  }| {__ | .-. \   \  {_ }| {_} || {__ .-._} }.-._} }| || |\  |\  {_ }   \  {_ }/  /\  \| |\ /| || {__ \n"
    "`-' `-'`-----'`-' ` `-'`----' `----'`-' `-'    `---' `-----'`----'`----' `----' `-'`-' `-' `---'     `---' `-'  `-'`-' ` `-'`----'\n"
]

# Rules of the game
rules = [
    "Welcome to the Number Guessing Game!",
    "",
    "Rules:",
    "--> You need to think of a number between 0 and 1000",
    "--> I will try to guess the number you're thinking of in 10 attempts.",
    "--> After each guess, tell me if I'm correct, or if your number is higher or lower than my guess.",
    "Let's begin!"
]

# Print ascii art
for line in ascii_art:
    print(line)

# Print rules in a box
max_length = max(len(rule) for rule in rules)
print('*' * (max_length + 4))
for rule in rules:
    print('* {:<{width}} *'.format(rule.strip(), width=max_length))
print('*' * (max_length + 4))
print("")

# Start the game
print("Time to choose a number! Can we continue? (Click ENTER when you are ready)")
input()

# Reset function to start the game again
def reset():
    print("Are you confused? Let's start again!")
    return 0, 1000, 1

min, max, count = reset()

# Main loop of the game
while True:
    # Check if the user is cheating
    if max < min:
        min, max, count = reset()
        continue
    
    # Guess the number
    attempt = (max + min) // 2
    
    # Print the guess and ask for feedback
    print(f"\nIs it {attempt}? Attempt number {count}")
    print("y - yes!\nl - lower!\nh - higer!")
    ans = input()
    
    # Check the user's feedback
    if ans == "y":
        break
    elif ans == "l":
        if min == ans:
            min, max, count = reset()
            continue;
        max = attempt - 1
        count += 1
        continue
    elif ans == "h":
        if max == ans:
            min, max, count = reset()
            continue
        min = attempt + 1
        count +=1
        continue
    else:
        print("Wrong input! Let's try one more time.")
        continue
    
# Print the result - END OF THE GAME
print(f"\nOh yes! I got it right in {count} attempts. :)")
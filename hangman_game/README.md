# Hangman Game

This Python script implements the classic game of Hangman. Players attempt to guess a hidden word by suggesting letters within a limited number of attempts. With each incorrect guess, a part of the hangman scaffold is built. The game challenges players to solve the word before the hangman is complete.

## Features

- ASCII art representation of the hangman scaffold.
- Random word selection from a predefined list.
- Interactive letter guessing with feedback on correct and incorrect choices.
- Validation to prevent repeated guesses and ensure valid inputs.
- Game over message with the correct word if the player loses.

## Installation

To play the game, you need Python 3.x installed on your computer. If you don't have Python installed, download and install it from [python.org](https://www.python.org/).

Clone this repository to your local machine:

```bash
git clone https://github.com/vapreace/Python-projects
````

Navigate to the `hangman_game` directory:

```bash
cd hangman_game
```

Run the Python script:

```bash
python hangman_game.py
```

## How to Play

1. **Run the Script**: Execute the script in your Python environment.
2. **Start the Game**: The script will select a random word, and the hangman scaffold will be displayed.
3. **Guess a Letter**: Input a letter to guess the word. The script will provide feedback on your choice.
4. **Winning the Game**: Continue guessing letters until you solve the word or run out of attempts.
5. **Game Over**: If you fail to guess the word within the attempts, the correct word will be revealed.

## Contributing

Contributions to the Hangman Game are welcome! If you have suggestions for improvements or bug fixes, feel free to open an issue or create a pull request.

## Credits

- Hangman ASCII art updated from [Chris Horton's GitHub](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c).
- ASCII text generated using [TAAG - Text to ASCII Art Generator](https://patorjk.com/software/taag/).
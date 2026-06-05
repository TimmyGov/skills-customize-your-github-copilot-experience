# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

In this assignment, you will build a command-line Hangman game in Python. You will practice using strings, loops, conditionals, and lists while creating a complete interactive program.

## 📝 Tasks

### 🛠️	Build the Core Hangman Game

#### Description
Create the main game loop for Hangman. The program should choose one word at random, ask the player to guess letters, and update the displayed progress after each guess.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list of words.
- Display the hidden word using underscores for letters not guessed yet (for example: `_ _ _ _ _`).
- Prompt the player to enter one letter at a time.
- Reveal correctly guessed letters in all matching positions.
- Track and display which letters have already been guessed.


### 🛠️	Add Win/Loss Logic and Game Feedback

#### Description
Finish the game by managing incorrect attempts and ending conditions. Provide clear messages so the player knows whether they won or lost.

#### Requirements
Completed program should:

- Start with a fixed number of incorrect attempts (for example, `6`) and decrease it only for wrong guesses.
- End the game with a win message when all letters in the word are guessed.
- End the game with a loss message when attempts reach `0` and display the correct word.
- Handle repeated guesses gracefully without crashing.
- Print a clear game status after each turn, including current word progress and attempts remaining.

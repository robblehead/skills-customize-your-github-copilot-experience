
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a simple Hangman game in Python to practice loops, conditionals, string handling, and user input. By the end, students should be able to manage game state and create clear win/lose outcomes.

## 📝 Tasks

### 🛠️ Build the Core Hangman Loop

#### Description
Create the main Hangman gameplay loop where the program chooses a word and the player guesses one letter at a time.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list.
- Display the current progress using underscores for unknown letters (for example: `_ _ a _ _`).
- Accept one letter guess at a time from the user.
- Reveal correctly guessed letters in all matching positions.
- Track and display remaining incorrect guesses.


### 🛠️ Add End Conditions and Feedback

#### Description
Finish the game by handling win/lose conditions and showing clear messages for each outcome.

#### Requirements
Completed program should:

- End with a win message when the full word is guessed.
- End with a lose message when the player runs out of attempts.
- Prevent duplicate guesses from incorrectly reducing attempts.
- Display the final word at the end of the game.
- Include at least one sample run in comments or documentation showing player interaction.

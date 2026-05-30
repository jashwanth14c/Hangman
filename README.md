

Hangman Game using Python

This is a simple command-line Hangman game built using Python. The player has to guess the hidden word letter by letter before running out of lives.

Features:
- Random word selection
- Shows first letter as a hint
- Tracks used letters
- 6 lives system
- Win/Lose condition

Requirements:
- Python 3
- random module (inbuilt)

How to run:
1. Open terminal
2. Go to project folder
   cd your-folder-name
3. Run the game
   python3 hangman.py

How it works:
- A random word is selected from word.py
- Player guesses one letter at a time
- Correct letters are revealed in the word
- Wrong guesses reduce lives
- Game ends when word is completed or lives reach 0

E

Win condition:
- You guessed all letters correctly

Lose condition:
- You used all 6 lives


# 🎯 Word Guessing Game (Python)

A simple **console-based word guessing game** developed using Python.  
The player selects a difficulty level and tries to guess the secret word with hints provided after each attempt.

---

## 🕹️ How the Game Works

1. The game welcomes the player.
2. The player selects a difficulty level:
   - Easy
   - Medium
   - Hard
3. A secret word is randomly selected based on the chosen level.
4. The player enters guesses.
5. After each incorrect guess, a hint is displayed:
   - Correct letters in the correct position are shown.
   - Incorrect letters are replaced with `_`.
6. The game continues until the correct word is guessed.
7. The total number of attempts is displayed at the end.

---

## 🧩 Difficulty Levels

| Level  | Sample Words |
|------|--------------|
| Easy | ball, road, apple, pen, dog |
| Medium | snake, laptop, elephant |
| Hard | access, bucket, build |

---

## 🛠️ Technologies Used

- Python 3
- `random` module
- Terminal / Console based input-output

---

## 📌 Sample Output

- Welcome to guessing game...
- Please choose the difficulty level (easy, medium, hard) :
- Enter difficulty level : easy
- Guess the word...
- Enter your word : road
- Hint : r___
- Enter your word : rock
- Hint : ro__
- Enter your word : road
- Congratulations ! You guessed correct word in 3 attempts.
- Game Over !

---

## 🚀 Features

- Random word selection
- Multiple difficulty levels
- Helpful hints after each attempt
- Counts number of attempts
- Beginner-friendly Python project

---

## 📚 Learning Outcomes

- Working with lists and strings
- Conditional statements
- Loops in Python
- Basic game logic

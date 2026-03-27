# Hangman-game---python
To design and implement an Advanced Hangman Game using Python. The system  allows the user to guess letters of a hidden word from different categories with limited  lives, hints, and a scoring system.
🎮 Advanced Hangman Game in Python

An interactive and feature-rich Hangman game built using Python. This project enhances the classic word-guessing game with categories, difficulty levels, hints, scoring, and visual stages.

🚀 Features
📂 Multiple Categories
Choose from Animals, Technology, and Movies
🎯 Difficulty Levels
Easy (8 lives)
Medium (6 lives)
Hard (4 lives)
💡 Hint System
Get hints when lives are low (with a small score penalty)
❤️ Life Tracking & Visual Hangman
ASCII art updates as you lose lives
⭐ Score System
Earn points for correct guesses, lose points for hints
🔁 Replay Option
Play multiple rounds without restarting the program
🛠️ Tech Used
Python (Core Concepts)
Random Module
CLI (Command Line Interface)
📸 Preview
Category: Animals
_ _ _ _ _ _ _

Guess a letter: e
Correct!

Word: e _ e _ _ _ _
Lives left: 6
Score: 10
💻 Full Code
import random

WORDS = {
    "Animals": ["elephant", "giraffe", "kangaroo", "alligator", "dolphin"],
    "Technology": ["python", "algorithm", "database", "encryption", "compiler"],
    "Movies": ["inception", "gladiator", "avatar", "titanic", "interstellar"]
}

HINTS = {
    "elephant": "Largest land animal",
    "giraffe": "Tallest animal",
    "kangaroo": "Australian jumper",
    "alligator": "Reptile with strong jaws",
    "dolphin": "Intelligent marine mammal",

    "python": "Popular programming language",
    "algorithm": "Step-by-step procedure",
    "database": "Stores structured data",
    "encryption": "Secures data",
    "compiler": "Translates code",

    "inception": "Dream within a dream",
    "gladiator": "Roman warrior movie",
    "avatar": "Blue aliens on Pandora",
    "titanic": "Famous ship tragedy",
    "interstellar": "Space-time travel movie"
}

STAGES = [
    """
     ------
     |    |
          |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    =========
    """
]

def play_game():
    print("\n🎮 Welcome to Advanced Hangman!\n")

    category = random.choice(list(WORDS.keys()))
    word = random.choice(WORDS[category])
    hint = HINTS[word]

    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    if difficulty == "easy":
        lives = 8
    elif difficulty == "medium":
        lives = 6
    else:
        lives = 4

    guessed_letters = []
    display = ["_" for _ in word]
    score = 0
    hint_used = False

    print(f"\n📂 Category: {category}")
    print(" ".join(display))

    while lives > 0 and "_" in display:
        guess = input("\n🔤 Guess a letter: ").lower()

        if guess in guessed_letters:
            print("⚠️ Already guessed!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
                    score += 10
        else:
            lives -= 1
            print("❌ Wrong guess!")

        print(STAGES[len(STAGES) - lives - 1])
        print("Word:", " ".join(display))
        print(f"❤️ Lives left: {lives}")
        print(f"⭐ Score: {score}")

        if lives <= 3 and not hint_used:
            use_hint = input("💡 Do you want a hint? (yes/no): ").lower()
            if use_hint == "yes":
                print("Hint:", hint)
                score -= 5
                hint_used = True

    if "_" not in display:
        print("\n🎉 You WON!")
        print(f"🏆 Final Score: {score}")
    else:
        print("\n💀 You LOST!")
        print(f"The word was: {word}")

while True:
    play_game()
    again = input("\n🔁 Play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing!")
        break
        <img width="1918" height="1005" alt="1" src="https://github.com/user-attachments/assets/6bdc2f9a-feb4-4b51-a52b-f8d81d3fd65c" />
        <img width="1918" height="1010" alt="2" src="https://github.com/user-attachments/assets/05afc1e1-2b9b-4613-b28d-53b72df20d8c" />

▶️ How to Run
Install Python (if not installed)
Save the file as hangman.py
Run the program:
python hangman.py
📈 Future Improvements
Add GUI using Tkinter or PyQt
Add multiplayer mode
Store high scores
Add more categories and words
🤝 Contributing

Feel free to fork this repo and improve the game. Contributions are always welcome!

📬 Feedback

If you liked this project, give it a ⭐ and share your suggestions!

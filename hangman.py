import random

# ===================== WORD DATABASE =====================
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

# ===================== HANGMAN STAGES =====================
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

# ===================== GAME FUNCTION =====================
def play_game():
    print("\n🎮 Welcome to Advanced Hangman!\n")

    # Choose category
    category = random.choice(list(WORDS.keys()))
    word = random.choice(WORDS[category])
    hint = HINTS[word]

    # Difficulty
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

    # ===================== GAME LOOP =====================
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

        # Hint option
        if lives <= 3 and not hint_used:
            use_hint = input("💡 Do you want a hint? (yes/no): ").lower()
            if use_hint == "yes":
                print("Hint:", hint)
                score -= 5
                hint_used = True

    # ===================== RESULT =====================
    if "_" not in display:
        print("\n🎉 You WON!")
        print(f"🏆 Final Score: {score}")
    else:
        print("\n💀 You LOST!")
        print(f"The word was: {word}")

# ===================== MAIN LOOP =====================
while True:
    play_game()
    again = input("\n🔁 Play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing!")
        break

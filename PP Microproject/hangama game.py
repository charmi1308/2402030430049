# Simple Hangman Game in Python

word = "python"
guessed = []
tries = 6

print("🎮 Welcome to Hangman!")
print("_ " * len(word))

while tries > 0:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("✅ Good guess!")
    else:
        tries -= 1
        print(f"❌ Wrong guess! Tries left: {tries}")

    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(display.strip())

    if all(letter in guessed for letter in word):
        print("🎉 Congratulations! You won!")
        break
else:
    print(f"💀 You lost. The word was: {word}")

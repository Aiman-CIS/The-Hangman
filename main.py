import random

def hangman():
    words = ['python', 'hangman', 'programming', 'computer', 'science']
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    
    while attempts > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"
        
        print("Guess the word:", guessed_word)
        print("Attempts remaining:", attempts)
 hangman()

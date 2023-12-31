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
        
        if guessed_word == word:
            print("Congratulations! You guessed the word correctly.")
            break
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print("Incorrect guess.")
        
        print()
    
    if attempts == 0:
        print("Sorry, you lost. The word was:", word)

hangman()

import random

words = [
    "python", "developer", "algorithm", "computer",
    "programming", "keyboard", "variable", "function",
    "database", "network", "compiler", "debugging"
]
def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def play_game():
    score = 0
    attempts_limit = 3
    
    print("Welcome to the Word Scramble Game!")
    print("Guess the correct word within 3 attempts.")

    
    while True:
        word = random.choice(words)
        scrambled = scramble_word(word)
        
        print("Scrambled Word:", scrambled)
        
        attempts = attempts_limit
        
        while attempts > 0:
            guess = input("Enter your guess: ").lower()
            
            if guess == word:
                print(" Correct! You earned 10 points.")
                score += 10
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f" Incorrect! Attempts left: {attempts}")
                else:
                    print(" No attempts left!")
        
        if attempts == 0:
            print(f"The correct word was: {word}")
        
        print(f"Current Score: {score}")
        
        choice = input("\nDo you want to play another round? (yes/no): ").lower()
        if choice != "yes":
            print("\n Final Score:", score)
            print("Thanks for playing!")
            break
play_game()
# Datamon Number Guesser
# By SK

import random

def main():
    
    print("Welcome to the Number guesser!\n\n")
    running = input("Ready to play? (Input yes/no): ")
    randNum = int(random.random() * 100)
    randRange = 50
    guesses = 0
    
    while running == "yes":
        
        print(f"The number is between {(randNum - randRange) - int(random.random()*5)} and {(randNum + randRange) + int(random.random()*5)}\n")
        guess = int(input("Guess an integer: "))
        
        if guess == randNum:
            print("Correct! Great Job! :D\n")
            guesses += 1
            print(f"Guesses taken: {guesses}")
            
            running = input("Wanna play again? (Input yes/no): ")
        
        else:
            print("Uh-oh, looks like you were wrong :(\n")
            randRange -= 10
            guesses += 1
        
    
    print("GG! Great Work!")
        
    
    
if __name__ == "__main__":
    main()
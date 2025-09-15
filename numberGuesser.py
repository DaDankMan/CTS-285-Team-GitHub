# Datamon Number Guesser

import random # Library that generates random numbers

def main():
    
    running = "yes"
    wins = 0
    totalGuesses = 0
    
    while running == "yes":
        
        randNum = int(random.random() * 100) # Randomly generates a number from 0-100
        randRange = 50 # Range that will be added and subtracted from randNum
        guesses = 0 # Self-explanatory
        
        print("\nWelcome to the Number guesser!\n")
        print(f"The number is between {(randNum - randRange) - int(random.random()*5)} and {(randNum + randRange) + int(random.random()*5)}\n")
        
        # Input validation
        valid = False
        while valid == False:
            try:
                guess = int(input("Guess a number: "))
                break
            
            except ValueError:         
                print("Invalid input. Please enter a valid integer")
        
        while guess != randNum: # Loop for when the user is wrong
            
            print("\nUh-oh, looks like you were wrong :(")
            guesses += 1
            totalGuesses += 1
            
            if randRange >= 10: # Makes sure the range doesn't get too small
                randRange -= 10
                
            print(f"The number is between {(randNum - randRange) - int(random.random()*5)} and {(randNum + randRange) + int(random.random()*5)}\n")
            
            # Input validation
            valid = False
            while valid == False:
                try:
                    guess = int(input("Guess a number: "))
                    break
                
                except ValueError:         
                    print("Invalid input. Please enter a valid integer") 
            
            # If the user is correct
        print("\nCorrect! You got the number!\n")
        print(f"Guesses taken: {guesses}")
        totalGuesses += 1
        wins += 1
        
        # If you wanna play again
        running = input("Wanna play again? (Input yes/no): ")

        
    # Ending stats
    print("\nGG! Great Work!")
    print(f"Wins: {wins}")
    print(f"Total Guesses: {totalGuesses}")
        
    
    
if __name__ == "__main__":
    main()
# Datamon Number Guesser

import random # Library that generates random numbers

def main():
    
    print("\nWelcome to the Number guesser!\n")
    
    running = "yes"
    wins = 0 # Counter that tracks how many times you've won
    totalGuesses = 0 # Counter that tracks how many guesses you've made in total
    
    while running == "yes":
        
        randNum = int(random.random() * 100) # Randomly generates an integer from 0-100
        randRange = 50 # Range that will be added and subtracted from randNum
        guesses = 0 # Counter that tracks how many guesses you've made this round
        
        print(f"The number is between {(randNum - randRange) - int(random.random()*5)} and {(randNum + randRange) + int(random.random()*5)}\n")
        
        # Input validation, makes sure guess is an integer
        valid = False
        while valid == False:
            try:
                guess = int(input("Guess a number: "))
                break
            
            except ValueError:         
                print("Invalid input. Please enter a valid integer")
        
        while guess != randNum: # Loop for when the user is wrong, kinda like input validation
            
            print("\nUh-oh, looks like you were wrong :(")
            guesses += 1
            totalGuesses += 1
            
            if randRange >= 20: # Makes sure the range doesn't go below 10
                randRange -= 10

            print(f"The number is between {(randNum - randRange) - int(random.random()*5)} and {(randNum + randRange) + int(random.random()*5)}\n")

            # Input validation, makes sure guess is an integer
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
        running = input("Wanna play again? (Input yes/no): ").lower() #.lower() ensures that case doesn't matter

        
    # Ending stats
    print("\nGG! Great Work!")
    print(f"Wins: {wins}")
    print(f"Total Guesses: {totalGuesses}")
        
    
    
if __name__ == "__main__":
    main()
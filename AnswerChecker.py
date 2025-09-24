import operator

def answerChecker():
    # Set up game rules, loop starting condition, score, and total questions values
    quit = False
    print("This game will check to see if you have the correct answer to your equation. Enter q to quit and get your final score.")
    score = 0
    totalQuest = 0

    

    # Start loop getting first equation    
    while not quit:
        equation = input("Enter your equation: ")
        num1 = equation.lstrip(' ')
        print(num1)
        operation = equation.rstrip()
        num2 = int(input("Second number: "))
        userAns = int(input("Your Answer: "))

        # Dictioinary to decide what operator is being used
        operatorsDict = {'+': operator.add(num1,num2), '-': operator.sub(num1,num2), '*': operator.mul(num1,num2),
                      '/': operator.floordiv(num1,num2)}
        ans = operatorsDict[operation]
        
        # Check if user gave correct answer and adjust score if they did
        if userAns == ans:
            print("You got it right!")
            score += 1
        else:
            print ("Your answer is incorrect.")
            # Ask if user wants to see the correct answer
            seeCorrect = input("Would you likme to see the correct answer? y/n: ")
            if seeCorrect == "y":
                print (ans)

        # Increment total questions, print score and total questions, ask user to  continue or end loop
        totalQuest += 1
        print("Your score is ", score, "out of" , totalQuest)
        x = input("Would you like to continue? Input 'q' to quit: ")
        if x == "q":
            quit = True
            print ("Thanks for playing!")


answerChecker()
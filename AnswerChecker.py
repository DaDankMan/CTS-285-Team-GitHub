import operator

def main():
    answerChecker()

def answerChecker():
    # Set up game rules, loop starting condition, score, and total questions values
    quit = False
    print("This game will check to see if you have the correct answer to your equation. Enter q to quit and get your final score.")
    score = 0
    totalQuest = 0

    

    # Start loop getting first equation    
    while not quit:
        equation = input("Enter your equation: ").strip()
        # Split user answer from equation
        try:
            expr, userAns = equation.split("=", 1)
            expr = expr.strip()
            userAns = userAns.strip()
        except Exception:
            print("Invalid equation, try again.")
            continue
        # Find operator in input equation
        try:
            operation = next(op for op in ['+', '-', '*', '/'] if op in expr)
        except StopIteration:
            print("Invalid equation. Please include +, -, *, or /.")
            continue
        # Split equation at operator
        try:
            num1, num2 = expr.split(operation)
            num1 = int(num1.strip())
            num2 = int(num2.strip())
            userAns = int(userAns)
        except Exception:
            print("Invalid equation, only two numbers and one operator. Try again.")
            continue
        

        # Dictioinary to complete operation
        operatorsDict = {'+': operator.add(num1,num2), '-': operator.sub(num1,num2), '*': operator.mul(num1,num2),
                      '/': operator.floordiv(num1,num2)}
        ans = operatorsDict[operation]
        
        # Check if user gave correct answer and adjust score if they did
        if userAns == ans:
            
            print("You got it right! Good job! 👍")
            score += 1
        else:
            print ("Your answer is incorrect.")
            # Ask if user wants to see the correct answer
            seeCorrect = input("Would you like to see the correct answer? y/n: ")
            if seeCorrect == "y":
                print (ans)

        # Increment total questions, print score and total questions, ask user to  continue or end loop
        totalQuest += 1
        print("Your score is ", score, "out of" , totalQuest)
        x = input("Would you like to continue? Type 'q' to quit: ")
        if x == "q":
            quit = True
            print ("Thanks for playing!")


if __name__ == "__main__":
    main()
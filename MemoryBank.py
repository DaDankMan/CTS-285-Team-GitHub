# MEMROY BANK CODE (IN PROGRESS)

import csv

def is_equation_correct(equation_str):
    """
    Checks if the equation string is ackshaully correct.
    Format is: expression = result (e.g., "1+1=2" or wtv)
    """
  
    if '=' not in equation_str:
        return False, None, None
    left, right = equation_str.split('=', 1)
    left = left.strip()
    right = right.strip()
    try:
        # Evaluates left side expression
        left_val = eval(left)
        # Evaluates right side expression (in case it's an expression, not just a number)
        right_val = eval(right)
        return left_val == right_val, left, right_val # guhh
    except Exception as e:
        return False, None, None

def input_equations(): #self-explanatory
    equations = []
    print("Please input 10 equations in the form 'expression = result' (e.g. 2+2=4):")
    while len(equations) < 10:
        eq = input(f"Equation {len(equations)+1}: ")
        correct, expr, ans = is_equation_correct(eq)
        if not correct:
            print("Incorrect equation or invalid format. Please try again.")
        else:
            equations.append((expr, ans))
    return equations

def save_to_csv(equations, filename="memory_bank.csv"): #also self-explanatory
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Expression", "Answer"])
        for expr, ans in equations:
            writer.writerow([expr, ans])
    print(f"Equations saved to {filename}")

def load_from_csv(filename="memory_bank.csv"): 
  # self-explanatory x3
  # add option to generate csv file or computer made equations..?? (mayhaps)
    equations = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expr = row["Expression"]
                ans = float(row["Answer"])
                equations.append((expr, ans))
    except FileNotFoundError:
        print(f"No saved file named {filename} found.")
    return equations

def practice(equations):
    print("\nLet's practice your equations!")
    score = 0
    for expr, ans in equations:
        user_ans = input(f"What is {expr}? ")
        try:
            user_ans_val = float(user_ans)
            if abs(user_ans_val - ans) < 1e-6:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. The correct answer is {ans}.")
        except ValueError:
            print(f"Invalid input. The correct answer is {ans}.")
    print(f"\nYour score: {score} out of {len(equations)}")

def main():
    print("Welcome to the Memory Bank Game!")
    choice = input("Do you want to (1) input new equations or (2) practice saved equations? Enter 1 or 2: ")
    if choice == '1':
        equations = input_equations()
        save_to_csv(equations)
        practice(equations)
    elif choice == '2':
        equations = load_from_csv()
        if equations:
            practice(equations)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()

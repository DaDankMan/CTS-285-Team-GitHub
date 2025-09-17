# MEMROY BANK CODE (IN PROGRESS)

import csv
import random

def main():
    # sub menu
    print("\nWelcome to the Memory Bank Game!\n")
    print("Choose an option:")
    print("---------------------")
    print("1. Input your own 10 equations")
    print("2. Generate 10 basic math equations")
    print("3. Practice from a saved file")
    print("---------------------\n")
    
    choice = input("Enter 1-3: ")
    
    if choice == '1':
        equations = input_equations()
        filename = input("Enter filename to save your equations (e.g. my_equations.csv): ").strip()
        
        if not filename:
            filename = "memory_bank.csv"
        save_to_csv(equations, filename)
        practice(equations)
        
    elif choice == '2':
        equations = generate_equations()
        filename = "generated_equations.csv"
        save_to_csv(equations, filename)
        print(f"Generated equations saved to {filename}")
        practice(equations)
        
    elif choice == '3':
        filename = input("Enter the filename of the saved equations (e.g. memory_bank.csv): ").strip()
        if not filename:
            print("No filename entered. Exiting.")
            return
            
        equations = load_from_csv(filename)
        if equations:
            practice(equations)
        else:
            print("No equations loaded. Exiting.")
    else:
        print("Invalid choice. Exiting.")


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
        left_val = eval(left)
        right_val = eval(right)
        return left_val == right_val, left, right_val
    except Exception:
        return False, None, None

def input_equations(): # uses format
    equations = []
    print("\nInput 10 equations in the form 'expression = result' (e.g. 2+2=4)\nINPUT:")
    while len(equations) < 10:
        eq = input(f"Equation {len(equations)+1}: ")
        correct, expr, ans = is_equation_correct(eq)
        if not correct:
            print("Uh-oh! Incorrect equation or invalid format.\nPlease try again.\n")
        else:
            equations.append((expr, ans))
    return equations

def save_to_csv(equations, filename="memory_bank.csv"): # saves to csv thingy
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Expression", "Answer"])
        for expr, ans in equations:
            writer.writerow([expr, ans])
    print(f"Equations saved to {filename}")

def load_from_csv(filename="memory_bank.csv"): # pulls from csv thingy
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

def generate_equations(): # auto gen math problems
    equations = []
    operations = ['+', '-', '*', '/']
    print("Generating 10 basic math equations...")
    while len(equations) < 10:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(operations)

        # used ai to amek decision shit
        if op == '/':
            a = a * b  # ensures integer division
        expr = f"{a} {op} {b}"
        try:
            ans = eval(expr)
            if op == '/':
                ans = round(ans, 2)
            else:
                ans = int(ans)
            equations.append((expr, ans))
        except Exception:
            continue
    return equations

def practice(equations):
    print("\nLet's practice your equations!\n")
    score = 0 # keepin score/results of practice 
    for expr, ans in equations:
        user_ans = input(f"What is {expr}? ")
        try:
            user_ans_val = float(user_ans)
            if abs(user_ans_val - ans) < 1e-2:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. The correct answer is {ans}.")
        except ValueError:
            print(f"Invalid input. The correct answer is {ans}.")
    print(f"\nYour score: {score} out of {len(equations)}")



if __name__ == "__main__":
    main()

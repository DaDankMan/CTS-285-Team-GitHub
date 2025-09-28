# MEMROY BANK CODE (IN PROGRESS)

import csv
import random
import sys

def main():
    while True:
        #SUB MENU
        print("\n⭐ Welcome to the Memory Bank Game! ⭐\n")
        print("Choose an option:")
        print("----------------------")
        print("1.) Input your own 10 equations")
        print("2.) Generate 10 basic math equations")
        print("3.) Practice from a saved file")
        print("4.) Exit") #returns to main MENU
        print("----------------------\n")
        
        choice = input("Enter a number (1-4): ").strip()
        
        if choice == '1':
            equations = input_equations()
            filename = input("Enter filename to save your equations\n(e.g. 'my_equations.csv', or 'my_equations.txt'): ").strip()
            if not filename:
                filename = "memory_bank.csv"
            save_to_csv(equations, filename)
            practice(equations)
            if not prompt_return_or_exit():
                break
        elif choice == '2':
            equations = generate_equations()
            filename = "generated_equations.csv"
            save_to_csv(equations, filename)
            print(f"Generated equations saved to {filename}! 👍")
            practice(equations)
            if not prompt_return_or_exit():
                break
        elif choice == '3':
            filename = input("Enter the filename of the saved equations (e.g. 'memory_bank.csv'): ").strip()
            if not filename:
                print("No filename entered. Returning to main menu.")
                continue
            equations = load_from_csv(filename)
            if equations is None:
                # if file isnt found, return to SUB MENU
                continue
            practice(equations)
            if not prompt_return_or_exit():
                break
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice...\nPlease enter 1, 2, 3, or 4. 🙄")


def is_equation_correct(equation_str):
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


def input_equations():
    equations = []
    print("Input 10 equations in the form 'expression = result' (e.g. 2+2=4): ")
    while len(equations) < 10:
        eq = input(f"\nEquation #{len(equations)+1}): ")
        correct, expr, ans = is_equation_correct(eq)
        if not correct:
            print("Uh-oh! 😱\nYou input an incorrect equation\nor used an invalid format. Please try again. ")
        else:
            equations.append((expr, ans))
    return equations


def save_to_csv(equations, filename="memory_bank.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Expression", "Answer"]) # so it can check da answer
        for expr, ans in equations:
            writer.writerow([expr, ans])
    print(f"Equations saved to '{filename}'")


def load_from_csv(filename="memory_bank.csv"):
    equations = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expr = row["Expression"]
                ans = float(row["Answer"])
                equations.append((expr, ans))
    except FileNotFoundError:
        print(f"No saved file named '{filename}' found.")
        return None
    return equations

def generate_equations():
    equations = []
    operations = ['+', '-', '*', '/']
    print("Generating 10 basic math equations...\n")
    print("----------------------------")
    while len(equations) < 10:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(operations)

        # AI decision structure
        if op == '/':
            a = a * b  # ensures integer division or wtv
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
    print("\nLet's practice your equations!")
    print("---------------------------------")
    score = 0
    total = len(equations)
    for expr, ans in equations:
        user_ans = input(f"What is '{expr}'?\nANSWER: ")
        try:
            user_ans_val = float(user_ans)
            if abs(user_ans_val - ans) < 1e-2:
                print("\nYippee! You are correct!\n")
                score += 1
            else:
                print(f"\nWrong. The correct answer is '{ans}.' 🤣\n")
        except ValueError:
            print(f"\nInvalid input. The correct answer is '{ans}.' 💀\n")
    accuracy = (score / total) * 100
    print(f"\nYour score: {score} out of {total} ({accuracy:.1f}%)")
    if score >= 6:
        print("Congratulations! You passed the practice. 🎉")
    else:
        print("Embarrasing... you scored less than 6.\nNot everyone can be a math wiz. Just keep practicing, bro... 😥\n")


def prompt_return_or_exit():
    while True:
        choice = input("\nEnter 'm' to return to the main menu or 'e' to exit: ").strip().lower()
        if choice == 'm':
            return True  # Return to menu
        elif choice == 'e':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please enter 'm' or 'e'...")

if __name__ == "__main__":
    main()

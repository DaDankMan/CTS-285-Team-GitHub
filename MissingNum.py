# By Damian Dotson
import random

def get_difficulty_range():
    print("Select difficulty level:")
    print("1. Easy (0 to 10)")
    print("2. Medium (0 to 30)")
    print("3. Hard (0 to 100)")
    print("4. EXTREME (-500 to 500)")

    while True:
        choice = input("Enter 1-4: ")
        if choice == '1':
            return 0, 10
        elif choice == '2':
            return 0, 30
        elif choice == '3':
            return 0, 100
        elif choice == '4':
            return -500, 500
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

def generate_missing_number_problem(min_val, max_val):
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)

    # Generate operands
    if operation == '+':
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        result = a + b
    elif operation == '-':
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        result = a - b
    elif operation == '*':
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        result = a * b
    elif operation == '/':
        # Avoid zero division
        b = random.randint(min_val if min_val != 0 else 1, max_val or 1)
        result = random.randint(min_val, max_val)
        a = b * result
    else:
        return None, None

    # Randomly choose position to hide (left, right, result)
    missing_position = random.choice(['left', 'right', 'result'])

    if missing_position == 'left':
        problem = f"_ {operation} {b} = {result}"
        correct_answer = a
    elif missing_position == 'right':
        problem = f"{a} {operation} _ = {result}"
        correct_answer = b
    else:  # result
        problem = f"{a} {operation} {b} = _"
        correct_answer = result

    return problem, correct_answer

# Main loop for user interaction
if __name__ == "__main__":
    print("🔢 Welcome to the Missing Number Box Game!")
    print("Fill in the blank (_) to complete the equation.\n")

    min_val, max_val = get_difficulty_range()

    for i in range(5):  # Ask 5 questions
        problem, correct_answer = generate_missing_number_problem(min_val, max_val)
        if problem is None:
            continue

        print(f"Problem {i+1}: {problem}")
        user_input = input("Your answer: ")

        # Try to convert input to float or int
        try:
            if '.' in user_input:
                user_answer = float(user_input)
            else:
                user_answer = int(user_input)
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue

        if abs(user_answer - correct_answer) < 0.001:  # account for float precision
            print("✅ Correct!\n")
        else:
            print(f"❌ Incorrect. The correct answer was {correct_answer}.\n")



import streamlit as st
import csv
import random
import os

# --- Utility functions (mostly unchanged) ---
def is_equation_correct(equation_str):
    if '=' not in equation_str:
        return False, None, None
    left, right = equation_str.split('=', 1)
    left, right = left.strip(), right.strip()
    try:
        left_val = eval(left)
        right_val = eval(right)
        return left_val == right_val, left, right_val
    except Exception:
        return False, None, None


def save_to_csv(equations, filename="memory_bank.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Expression", "Answer"])
        for expr, ans in equations:
            writer.writerow([expr, ans])


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
        st.error(f"No saved file named '{filename}' found.")
        return None
    return equations


def generate_equations():
    equations = []
    operations = ['+', '-', '*', '/']
    while len(equations) < 10:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(operations)
        if op == '/':
            a = a * b
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


# --- Streamlit App ---
st.title("⭐ Memory Bank Game ⭐")

# Persistent state
if "page" not in st.session_state:
    st.session_state.page = "menu"
if "equations" not in st.session_state:
    st.session_state.equations = []
if "score" not in st.session_state:
    st.session_state.score = 0

# --- Menu Page ---
if st.session_state.page == "menu":
    st.subheader("Main Menu")
    st.write("Choose an option below 👇")

    if st.button("1️⃣ Input Your Own 10 Equations"):
        st.session_state.page = "input_equations"

    if st.button("2️⃣ Generate 10 Basic Math Equations"):
        st.session_state.equations = generate_equations()
        save_to_csv(st.session_state.equations, "generated_equations.csv")
        st.session_state.page = "practice"

    if st.button("3️⃣ Practice from a Saved File"):
        st.session_state.page = "load_file"

    if st.button("4️⃣ Exit"):
        st.success("Goodbye! 👋")
        st.stop()

# --- Input Equations Page ---
elif st.session_state.page == "input_equations":
    st.subheader("✏️ Enter 10 Equations (e.g. 2+2=4)")
    eq_inputs = []
    with st.form("input_form"):
        for i in range(10):
            eq_inputs.append(st.text_input(f"Equation #{i+1}"))
        submitted = st.form_submit_button("Save & Practice")

    if submitted:
        valid_eqs = []
        for eq in eq_inputs:
            correct, expr, ans = is_equation_correct(eq)
            if correct:
                valid_eqs.append((expr, ans))
        if len(valid_eqs) == 10:
            save_to_csv(valid_eqs, "memory_bank.csv")
            st.session_state.equations = valid_eqs
            st.session_state.page = "practice"
        else:
            st.error("Please make sure all 10 equations are valid!")

# --- Load File Page ---
elif st.session_state.page == "load_file":
    st.subheader("📂 Load Saved Equations")
    filename = st.text_input("Enter the filename (e.g. memory_bank.csv):", "memory_bank.csv")
    if st.button("Load"):
        eqs = load_from_csv(filename)
        if eqs:
            st.session_state.equations = eqs
            st.session_state.page = "practice"

    if st.button("⬅️ Back to Menu"):
        st.session_state.page = "menu"

# --- Practice Page ---
elif st.session_state.page == "practice":
    st.subheader("🧠 Practice Time!")
    score = 0
    total = len(st.session_state.equations)

    with st.form("practice_form"):
        user_answers = []
        for expr, ans in st.session_state.equations:
            user_ans = st.text_input(f"What is '{expr}'?")
            user_answers.append((expr, ans, user_ans))
        submitted = st.form_submit_button("Check Answers")

    if submitted:
        for expr, ans, user_ans in user_answers:
            try:
                if abs(float(user_ans) - ans) < 1e-2:
                    score += 1
            except:
                continue
        st.session_state.score = score
        st.session_state.page = "results"

# --- Results Page ---
elif st.session_state.page == "results":
    total = len(st.session_state.equations)
    score = st.session_state.score
    accuracy = (score / total) * 100
    st.subheader("📊 Results")
    st.write(f"Your score: **{score} / {total}** ({accuracy:.1f}%)")

    if score >= 6:
        st.success("🎉 Congratulations! You passed!")
    else:
        st.warning("😥 You scored less than 6. Keep practicing!")

    if st.button("⬅️ Return to Menu"):
        st.session_state.page = "menu"
    if st.button("🚪 Exit"):
        st.success("Goodbye! 👋")
        st.stop()
import streamlit as st
import operator

# ...existing code...

# Initialize session state variables to persist values between interactions
if "score" not in st.session_state:
    st.session_state.score = 0
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# New session keys for showing correct answer
if "show_correct" not in st.session_state:
    st.session_state.show_correct = False
if "correct_to_show" not in st.session_state:
    st.session_state.correct_to_show = ""

# Callback to show correct answer
def _show_correct_callback(answer):
    st.session_state.show_correct = True
    st.session_state.correct_to_show = answer

# Callback to restart the game
def _restart_callback():
    st.session_state.score = 0
    st.session_state.total_questions = 0
    st.session_state.game_over = False
    st.session_state.show_correct = False
    st.session_state.correct_to_show = ""

st.title("🧠 Equation Answer Checker")
st.write("Enter a basic equation (e.g., `3 + 5 = 8`) and see if you got it right! Supports +, -, *, and / (integer division).")

# Quit button
if st.button("Quit Game"):
    st.session_state.game_over = True

if not st.session_state.game_over:
    # Restart button available during the game
    if st.button("Restart Game"):
        _restart_callback()

    # Equation input field
    equation = st.text_input("Enter your equation here:", placeholder="e.g. 7 * 6 = 42")

    if st.button("Check Answer"):
        # clear previous shown answer when checking a new equation
        st.session_state.show_correct = False
        if "=" not in equation:
            st.warning("❌ Invalid format. Make sure to include `=` in your equation.")
        else:
            expr, userAns = equation.split("=", 1)
            expr = expr.strip()
            userAns = userAns.strip()

            # Detect the operator
            try:
                operation = next(op for op in ['+', '-', '*', '/'] if op in expr)
            except StopIteration:
                st.error("Invalid equation. Please include +, -, *, or /.")
                st.stop()

            # Split into numbers
            try:
                num1, num2 = expr.split(operation)
                num1 = int(num1.strip())
                num2 = int(num2.strip())
                userAns = int(userAns)
            except Exception:
                st.error("Invalid equation, only two integers and one operator. Try again.")
                st.stop()

            # Evaluate the answer safely
            try:
                if operation == '+':
                    correct_ans = operator.add(num1, num2)
                elif operation == '-':
                    correct_ans = operator.sub(num1, num2)
                elif operation == '*':
                    correct_ans = operator.mul(num1, num2)
                elif operation == '/':
                    # integer division, handle division by zero
                    correct_ans = operator.floordiv(num1, num2)
                else:
                    st.error("Unsupported operator.")
                    st.stop()
            except ZeroDivisionError:
                st.error("Division by zero is not allowed.")
                st.stop()

            # Check correctness
            if userAns == correct_ans:
                st.success("✅ You got it right! Good job!")
                st.session_state.score += 1
            else:
                st.error("❌ Your answer is incorrect.")
                # show correct answer button with working callback and correct variable
                st.button("Show correct answer", on_click=_show_correct_callback, args=(correct_ans,))

            # Display correct answer if requested
            if st.session_state.get("show_correct"):
                st.info(f"Correct answer: {st.session_state.get('correct_to_show')}")

            st.session_state.total_questions += 1

    # Display score
    st.write(f"**Score:** {st.session_state.score} out of {st.session_state.total_questions}")

else:
    st.subheader("🎯 Final Score")
    st.write(f"You scored **{st.session_state.score}** out of **{st.session_state.total_questions}** questions.")
    if st.button("Restart Game"):
        _restart_callback()
# ...existing code...
```# filepath: /workspaces/CTS-285-Team-GitHub/answerchecker_streamlit.py
import streamlit as st
import operator

# ...existing code...

# Initialize session state variables to persist values between interactions
if "score" not in st.session_state:
    st.session_state.score = 0
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# New session keys for showing correct answer
if "show_correct" not in st.session_state:
    st.session_state.show_correct = False
if "correct_to_show" not in st.session_state:
    st.session_state.correct_to_show = ""

# Callback to show correct answer
def _show_correct_callback(answer):
    st.session_state.show_correct = True
    st.session_state.correct_to_show = answer

# Callback to restart the game
def _restart_callback():
    st.session_state.score = 0
    st.session_state.total_questions = 0
    st.session_state.game_over = False
    st.session_state.show_correct = False
    st.session_state.correct_to_show = ""

st.title("🧠 Equation Answer Checker")
st.write("Enter a basic equation (e.g., `3 + 5 = 8`) and see if you got it right! Supports +, -, *, and / (integer division).")

# Quit button
if st.button("Quit Game"):
    st.session_state.game_over = True

if not st.session_state.game_over:
    # Restart button available during the game
    if st.button("Restart Game"):
        _restart_callback()

    # Equation input field
    equation = st.text_input("Enter your equation here:", placeholder="e.g. 7 * 6 = 42")

    if st.button("Check Answer"):
        # clear previous shown answer when checking a new equation
        st.session_state.show_correct = False
        if "=" not in equation:
            st.warning("❌ Invalid format. Make sure to include `=` in your equation.")
        else:
            expr, userAns = equation.split("=", 1)
            expr = expr.strip()
            userAns = userAns.strip()

            # Detect the operator
            try:
                operation = next(op for op in ['+', '-', '*', '/'] if op in expr)
            except StopIteration:
                st.error("Invalid equation. Please include +, -, *, or /.")
                st.stop()

            # Split into numbers
            try:
                num1, num2 = expr.split(operation)
                num1 = int(num1.strip())
                num2 = int(num2.strip())
                userAns = int(userAns)
            except Exception:
                st.error("Invalid equation, only two integers and one operator. Try again.")
                st.stop()

            # Evaluate the answer safely
            try:
                if operation == '+':
                    correct_ans = operator.add(num1, num2)
                elif operation == '-':
                    correct_ans = operator.sub(num1, num2)
                elif operation == '*':
                    correct_ans = operator.mul(num1, num2)
                elif operation == '/':
                    # integer division, handle division by zero
                    correct_ans = operator.floordiv(num1, num2)
                else:
                    st.error("Unsupported operator.")
                    st.stop()
            except ZeroDivisionError:
                st.error("Division by zero is not allowed.")
                st.stop()

            # Check correctness
            if userAns == correct_ans:
                st.success("✅ You got it right! Good job!")
                st.session_state.score += 1
            else:
                st.error("❌ Your answer is incorrect.")
                # show correct answer button with working callback and correct variable
                st.button("Show correct answer", on_click=_show_correct_callback, args=(correct_ans,))

            # Display correct answer if requested
            if st.session_state.get("show_correct"):
                st.info(f"Correct answer: {st.session_state.get('correct_to_show')}")

            st.session_state.total_questions += 1

    # Display score
    st.write(f"**Score:** {st.session_state.score} out of {st.session_state.total_questions}")

else:
    st.subheader("🎯 Final Score")
    st.write(f"You scored **{st.session_state.score}** out of **{st.session_state.total_questions}** questions.")
    if st.button("Restart Game"):
        _restart_callback()
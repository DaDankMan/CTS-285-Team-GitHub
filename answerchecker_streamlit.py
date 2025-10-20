import streamlit as st
import operator

# Initialize session state variables to persist values between interactions
if "score" not in st.session_state:
    st.session_state.score = 0
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title("🧠 Equation Answer Checker")
st.write("Enter a basic equation (e.g., `3 + 5 = 8`) and see if you got it right! Supports +, -, *, and / (integer division).")

# Quit button
if st.button("Quit Game"):
    st.session_state.game_over = True

if not st.session_state.game_over:
    # Equation input field
    equation = st.text_input("Enter your equation here:", placeholder="e.g. 7 * 6 = 42")

    if st.button("Check Answer"):
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
                st.error("Invalid equation, only two numbers and one operator. Try again.")
                st.stop()

            # Evaluate the answer
            operatorsDict = {
                '+': operator.add(num1, num2),
                '-': operator.sub(num1, num2),
                '*': operator.mul(num1, num2),
                '/': operator.floordiv(num1, num2),
            }
            correct_ans = operatorsDict[operation]

            # Check correctness
            if userAns == correct_ans:
                st.success("✅ You got it right! Good job!")
                st.session_state.score += 1
            else:
                st.error("❌ Your answer is incorrect.")
                if st.checkbox("Show correct answer"):
                    st.info(f"The correct answer is: **{correct_ans}**")

            st.session_state.total_questions += 1

    # Display score
    st.write(f"**Score:** {st.session_state.score} out of {st.session_state.total_questions}")

else:
    st.subheader("🎯 Final Score")
    st.write(f"You scored **{st.session_state.score}** out of **{st.session_state.total_questions}** questions.")
    if st.button("Restart Game"):
        st.session_state.score = 0
        st.session_state.total_questions = 0
        st.session_state.game_over = False
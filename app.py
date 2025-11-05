import streamlit as st
from typing import Tuple
import tempfile
import traceback

st.set_page_config(page_title="Datamon Answer Checker", layout="centered")

st.title("Datamon Answer Checker — Web Interface")
st.markdown(
    """
A quick web front-end for your Datamon answer checker (prototype).
Usage: paste or upload the Datamon input, enter the candidate answer, then click Check.
"""
)

with st.expander("Instructions / Notes", expanded=False):
    st.write(
        """
This is a prototype UI. Replace check_answer() with your real Datamon checking routine.
For heavy initialization (models, large lookups), wrap that code with st.cache_resource or expose it via a small API to avoid rerunning on every interaction.
This app runs locally with streamlit run app.py. See README.md for full instructions.
"""
    )

# Input area: Datamon text or file
st.header("1) Provide Datamon input")
datamon_text = st.text_area("Paste Datamon input here (optional)", height=200)
uploaded_file = st.file_uploader(
    "Or upload a file containing the Datamon input", type=["txt", "md", "json", "csv"]
)


def read_uploaded_file(u):
    if not u:
        return ""
    try:
        raw = u.read()
        # uploaded_file.read() returns bytes for text files in streamlit
        if isinstance(raw, bytes):
            return raw.decode(errors="replace")
        return str(raw)
    except Exception:
        return ""


if not datamon_text and uploaded_file:
    datamon_text = read_uploaded_file(uploaded_file)

# Input area: answer
st.header("2) Provide Candidate Answer")
candidate_answer = st.text_input("Candidate answer (string)", "")

# Options
st.markdown("Options")
explain = st.checkbox("Return explanation", value=True)
normalize_case = st.checkbox("Case-insensitive comparison", value=True)
trim_whitespace = st.checkbox("Trim whitespace before comparison", value=True)

# Helper: placeholder checker
def simple_normalize(s: str, case: bool, trim: bool) -> str:
    if s is None:
        return ""
    if trim:
        s = s.strip()
    if case:
        s = s.lower()
    return s


def check_answer(datamon: str, answer: str, opts: dict) -> Tuple[bool, str]:
    """
    Placeholder check function.

    **INTEGRATION POINT**:
    Replace the body of this function with a call into your existing Datamon console checker.
    Example:
        from datamon_checker import DatamonChecker
        checker = DatamonChecker.load_from_config(...)
        ok, explanation = checker.check(datamon, answer)

    For now, this function implements a simple normalized-string equality check and returns
    a short explanation. This is intentional so you can test the UI without your console app.
    """
    try:
        if not datamon:
            return False, "No Datamon input provided."
        if not answer:
            return False, "No candidate answer provided."

        a = simple_normalize(answer, opts["case_insensitive"], opts["trim"])
        # VERY SIMPLE heuristic: extract the "expected" answer if the datamon contains a line like "EXPECTED: <value>"
        expected = None
        for line in datamon.splitlines():
            if "EXPECTED:" in line.upper():
                # naive parse after colon
                parts = line.split(":", 1)
                if len(parts) > 1:
                    expected = parts[1].strip()
                    break
        if expected is None:
            # fallback: use the last non-empty line as expected
            lines = [ln.strip() for ln in datamon.splitlines() if ln.strip()]
            if lines:
                expected = lines[-1]

        if expected is None:
            # can't determine an expected value; fail safely but return helpful explanation
            return (
                False,
                "Could not detect an expected answer in the Datamon input. "
                "Look for a line like `EXPECTED: <value>` or paste the expected value into the Datamon input.",
            )

        expected_norm = simple_normalize(expected, opts["case_insensitive"], opts["trim"])

        correct = (a == expected_norm)
        explanation = f"Expected (parsed): `{expected}`\nYour normalized answer: `{a}`\nNormalized expected: `{expected_norm}`"
        return correct, explanation
    except Exception as e:
        tb = traceback.format_exc()
        return False, f"Checker runtime error: {e}\n\n{tb}"


# Action
if st.button("Check"):
    opts = {
        "case_insensitive": normalize_case,
        "trim": trim_whitespace,
        "explain": explain,
    }
    try:
        ok, explanation = check_answer(datamon_text, candidate_answer, opts)
        if ok:
            st.success("✔ Correct")
        else:
            st.error("✖ Incorrect / Not validated")
        if explain:
            st.markdown("Explanation")
            st.code(explanation)
    except Exception as e:
        st.exception(e)

# Footer / debug
with st.expander("Developer / Integration notes", expanded=False):
    st.markdown(
        """
Integration guidance:
Replace check_answer() with a wrapper around your Datamon console logic.
If your Datamon console is a CLI binary, consider wrapping it with subprocess.run and parsing output, or better, factor the checking logic into a small Python module that both the console and web UI can import.
Caching:
Use @st.cache_resource to cache heavy resources (models, DB connections).
"""
    )

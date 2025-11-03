# streamlit_tic_tac_toe.py

import streamlit as st

# --- Helper Functions ---

def init_game():
    """Initialize the board and player states in session."""
    if "board" not in st.session_state:
        st.session_state.board = [[" " for _ in range(3)] for _ in range(3)]
    if "current_player" not in st.session_state:
        st.session_state.current_player = "X"
    if "winner" not in st.session_state:
        st.session_state.winner = None

def check_winner(board):
    """Return 'X', 'O', or None depending on board state."""
    lines = [
        board[0], board[1], board[2],
        [board[i][0] for i in range(3)],
        [board[i][1] for i in range(3)],
        [board[i][2] for i in range(3)],
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)]
    ]
    for line in lines:
        if line.count(line[0]) == 3 and line[0] != " ":
            return line[0]
    return None

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def make_move(r, c):
    """Handle player move logic."""
    if st.session_state.winner:
        return
    board = st.session_state.board
    if board[r][c] == " ":
        board[r][c] = st.session_state.current_player
        winner = check_winner(board)
        if winner:
            st.session_state.winner = winner
        elif is_draw(board):
            st.session_state.winner = "Draw"
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

def reset_game():
    for key in ["board", "current_player", "winner"]:
        if key in st.session_state:
            del st.session_state[key]
    init_game()

# --- Streamlit UI ---

st.title("🎮 Tic Tac Toe")
st.caption("Built with Streamlit")

init_game()

st.write(f"**Current Player:** {st.session_state.current_player}")

# Game Board
for r in range(3):
    cols = st.columns(3)
    for c in range(3):
        cell_value = st.session_state.board[r][c]
        btn_label = cell_value if cell_value != " " else " "
        cols[c].button(
            btn_label,
            key=f"cell_{r}_{c}",
            on_click=make_move,
            args=(r, c),
            use_container_width=True
        )

# Result Message
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("It's a Draw!")
    else:
        st.success(f"🎉 Player {st.session_state.winner} wins!")

st.button("🔄 Restart Game", on_click=reset_game)
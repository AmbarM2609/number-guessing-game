import streamlit as st

def header():
    st.title("🎯 Number Guessing Game")
    st.markdown("Try your luck. Guess wisely.")

def difficulty_selector(difficulties):
    st.header("Game Settings")

    diff = st.selectbox("Choose Difficulty", list(difficulties.keys()))
    start = st.button("Start New Game")

    return diff, start

def metrics(low, high, attempts_left):
    col1, col2 = st.columns(2)
    col1.metric("Range", f"{low} – {high}")
    col2.metric("Attempts Left", attempts_left)

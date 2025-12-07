import streamlit as st

def guess_input(low, high):
    return st.number_input(
        "Enter your guess:",
        min_value=low,
        max_value=high,
        step=1
    )

def submit_button():
    return st.button("Submit Guess")

def play_again():
    return st.button("Play Again")

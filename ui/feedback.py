import streamlit as st

def show_progress(attempts, max_attempts):
    st.progress(attempts / max_attempts)

def success(secret):
    st.success(f"🎉 Correct! The number was **{secret}**.")
    st.balloons()

def wrong_hint(direction):
    if direction == "low":
        st.warning("📉 Too low.")
    else:
        st.warning("📈 Too high.")

def game_over(secret):
    st.error(f"😢 Out of attempts! The number was **{secret}**.")

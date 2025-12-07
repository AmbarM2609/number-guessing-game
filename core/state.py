import streamlit as st

def init_game_state():
    defaults = {
        "low": None,
        "high": None,
        "max_attempts": None,
        "secret": None,
        "attempts": 0,
        "active": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def set_game_state(game):
    for key, value in game.items():
        st.session_state[key] = value

def reset_state():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

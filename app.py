import streamlit as st
from core.config import DIFFICULTIES
from core.logic import start_new_game, check_guess
from core.state import init_game_state, set_game_state, reset_state
from ui.layout import header, difficulty_selector, metrics
from ui.widgets import guess_input, submit_button, play_again
from ui.feedback import success, wrong_hint, game_over, show_progress

st.set_page_config(page_title="Number Guessing", page_icon="🎯")

def main():
    init_game_state()
    header()

    difficulty, start = difficulty_selector(DIFFICULTIES)

    # Start new game
    if start:
        game = start_new_game(DIFFICULTIES[difficulty])
        set_game_state(game)
        st.rerun()

    # Game not started
    if not st.session_state.active:
        st.info("Select difficulty and click *Start New Game*.")
        return

    # Stats
    attempts_left = st.session_state.max_attempts - st.session_state.attempts
    metrics(st.session_state.low, st.session_state.high, attempts_left)
    show_progress(st.session_state.attempts, st.session_state.max_attempts)

    # Guess Input
    guess = guess_input(st.session_state.low, st.session_state.high)
    submit = submit_button()

    if submit:
        st.session_state.attempts += 1
        result = check_guess(st.session_state.secret, guess)

        if result == "correct":
            success(st.session_state.secret)
            st.session_state.active = False

        else:
            wrong_hint(result)

        if st.session_state.attempts >= st.session_state.max_attempts and st.session_state.active:
            game_over(st.session_state.secret)
            st.session_state.active = False

    # Restart
    if not st.session_state.active:
        if play_again():
            reset_state()
            st.rerun()

if __name__ == "__main__":
    main()

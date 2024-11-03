import streamlit as st
import random
from utils.lit import add_guess, check_guess, get_key, set_guessed, init_key, set_last_guess
from utils.constants import INTRO_CONTENT, TITLE

init_key("max_val", random.randint(100, 999))
init_key("guessed", "? ? ?")
stats: dict = {"guesses": [], "games": 0}
init_key("stats", stats)
init_key("to_guess", str(random.randint(1, st.session_state.max_val)).rjust(3, "0"))

st.title(TITLE)

guess_num = st.chat_input("Your guess")
guess = str(guess_num).rjust(3, "0")
add_guess(get_key("to_guess"), guess_num)


set_guessed(guess)


st.markdown(INTRO_CONTENT.format(max_val=st.session_state.max_val, guessed=st.session_state.guessed))

set_last_guess(guess_num)
check_guess(guess)

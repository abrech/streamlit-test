import streamlit as st
import pandas as pd

# TODO keine doppelten guesses pro session, oder id für guesses stats

def set_key(key, val):
    st.session_state[key] = val

def init_key(key, val):
    if key not in st.session_state:
        st.session_state[key] = val

def get_key(key):
    if key in st.session_state:
        return st.session_state[key]
    return None

def clear_keep_stats():
    stats = get_key("stats")
    st.session_state.clear()
    init_key("stats", stats)

def check_guess(guess):
    if guess != "None" and guess != st.session_state.to_guess:
        st.write("Close!")
    elif guess == st.session_state.to_guess:
        st.write("Wow! That's right. Just type another guess to play again!")
        stats: dict = get_key("stats")
        stats["games"] = stats.get("games", 0) + 1
        clear_keep_stats()

def set_last_guess(guess_num):
    if guess_num and guess_num.isnumeric():
        st.session_state.last_guess = guess_num

def set_guessed(guess):
    for i, c in enumerate(st.session_state.to_guess):
        if c == guess[i]:
            st.session_state.guessed = st.session_state.guessed[:i*2] + c + st.session_state.guessed[(i*2) + 1:]

def add_guess(to_guess: str, guess: str):
    if not guess or (guess and guess == "None"):
        return
    stats: dict = get_key("stats")
    if to_guess.isnumeric() and guess.isnumeric():
        stats["guesses"].append({"to_guess": int(to_guess), "guess": int(guess)})

def create_df(stats: dict):
    guesses = stats.get("guesses")
    goal_count = dict()
    for guess in guesses:
        goal_count[guess.get("to_guess")] = goal_count.get(guess.get("to_guess"), 0) + 1
    if len(goal_count.values()) == 0:
        return
    max_guesses = max(goal_count.values())
    guess_count = dict()
    i = 1
    while i <= max_guesses:
        guess_count[i] = list(goal_count.values()).count(i)
        i += 1
    df = pd.DataFrame.from_dict(guess_count, orient='index', columns=['Value'])
    df.index.name = 'Key'
    df.reset_index(inplace=True)
    return df.set_index("Key")


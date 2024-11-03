import streamlit as st
import random

a=5
st.title("My fabulous number guessing game: NumWhy?")

st.write(f"This is my first web {a}pp.")

# st.camera_input("Kamera")

# program reruns on user input
g = st.number_input(label="hi", step=1)
rnd = random.randint(1,10)
st.write(f"Random: {rnd}")

st.write(g)

# session dictionary session_state
if "rnd" not in st.session_state:
    st.session_state.rnd = random.randint(1, 100)
st.write(f"Not random: {st.session_state.rnd}")

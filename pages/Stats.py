import streamlit as st
import pandas as pd

from utils.constants import STATS_TITLE
from utils.lit import create_df, get_key

stats = get_key("stats")

st.title(STATS_TITLE)

if not stats or stats.get("games", 0) == 0:
    st.markdown("### Seems like you haven't played any games yet!")
else:
    st.write("Total games played: " + str(stats.get("games", 0)))
    st.bar_chart(create_df(stats), y_label="Amount of times", x_label="Guesses needed")
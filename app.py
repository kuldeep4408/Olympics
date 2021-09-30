from typing import Text
import streamlit as st
import pandas as pd

st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall-Analysis','Country-Wise-Analysis','Athlete-Wise-Analysis')
)

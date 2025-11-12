import streamlit as st
import pandas as pd
import numpy as np

st.title("Sidebar")
st.write("Kelompok: 16")
st.markdown("""
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- AZRIL PUTRA SYAHRI - 0110222197
- BAGUS ACHMAD HIDAYAT - 0110222002 
""")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User?", ("Yes", "No"))
st.sidebar.slider("Select a Number", 0, 10)
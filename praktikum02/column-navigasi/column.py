import streamlit as st
import pandas as pd
import numpy as np

st.title("Column")
st.write("Kelompok: 16")
st.markdown("""
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- AZRIL PUTRA SYAHRI - 0110222197
- BAGUS ACHMAD HIDAYAT - 0110222002 
""")

col1, col2, = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("../../praktikum01/assets/jk_1.jpg")
col2.write("Ini adalah kolom kedua")
col2.image("../../praktikum01/assets/jk_2.jpg")


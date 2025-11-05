# import library
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Praktikum 01 Visualisasi Data")
st.subheader("Bagian 4-buttons-sliders")
st.markdown("""
KELOMPOK 16
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- BAGUS ACHMAD HIDAYAT - 0110222002
- AZRIL PUTRA SYAHRI - 0110222197
""")

# Buttons dan sliders pada streamlit adalah elemen yang digunakan untuk memicu suatu aksi ketika pengguna mengklik tombol tersebut
st.title('Creating a Button')
# Defineing a Button
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')

# Radio Buttons pada steamlit elemen yang memungkinkan pengguna memilih salah satu opsi dari beberapa pilihan yang tersedia.
st.title('Creating Radio Buttons')
# Defineing a Radio Button
gender = st.radio('Select your Gender',
('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Famele':
    st.write('You have selected Female.')
else:
    st.write('You have selected Others.')

# Check Boxes pada Streamlit adalah elemenyang memungkinkan pengguna untuk memilih atau tidak memilih opsi tertentu.
st.title('Creating Checkboxes')
st.write('Select your Hobbies')
# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

# Drop-Downs pada Streamlit adalah elemen yang memungkinkan pengguna memilih satu opsi dari daftar pilihan yang tersedia
st.title('Creating Dropdown')
# Creating Dropdown
hobby = st.selectbox('Choose your hobby:',
('Books', 'Movies',  'Sports'))

# Multiselects pada Streamlit adalah elemenyang memungkinkan pengguna memilih beberapa opsi dari daftar yang tersedia.
st.title('Milti-Select')
# Defining Multi-select with Pre-selection
hobbies = st.multiselect(
'What are your Hobbies',
['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
['Reading', 'Playing'])

# Download Buttons pada streamlit adalah elemen  yang memungkinkan pengguna untuk mengunduh file langsung dari aplikasi.
st.title('Download Button')
# Creating Download Button
down_btn = st.download_button(
label = 'Download Image',
data=open('assets/jk_1.jpg', 'rb'),
file_name='jungkooklove.jpg',
mime='image/jpg'
)

# Progress Bars dalam streamlit adalah elemen visual yang digunakan untuk menunjukkan progres atau kemajuan dari suatu proses di aplikasi Anda. 
import time 
st.title('Progress Bar')
# Defining Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complate')

# Spinners pada streamlit adalah elemen visual yang digunakan untuk memberikan indikasi bahwa suatu proses sedang berlangsung. 
import time
st.title('Spinner')
# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hallo Data Scientists')
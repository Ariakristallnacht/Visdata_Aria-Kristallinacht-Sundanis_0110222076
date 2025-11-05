# import library
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Praktikum 01 Visualisasi Data")
st.subheader("Bagian 2-data-elements")
st.markdown("""
KELOMPOK 16
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- BAGUS ACHMAD HIDAYAT - 0110222002
- AZRIL PUTRA SYAHRI - 0110222197
""")

# DataFrame : stuktur data
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

# Menampilkan dataframe
st.dataframe(df)

# Highlifht Nilai Minimum
st.subheader("Highlight Minimum Value di DataFrame")

# highlight nilai terkecil disetiap kolom dataframe
# axis 
st.dataframe(df.style.highlight_min(axis=0))

# Tabel Statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

# Menampilkan tabel statis
st.table(df)

# Metrics : komponen tampilan angka penting
st.subheader("Metrics")
# Menampilkan metrik tunggal  (nilai utama + )
st.metric(label="Temperature", value="31 C", delta="1.2 C") # kenaikan 1.2 C

# Matric sesuai delta_color
# delta_color digunakan untuk memberi warna sesuai arah perubahan:
# "normal" (default): naik -> gijau, turun -> merah 
# "invers" : kebalikannya (naik -> merah)
# "off" : tidak menampilkan warna perubahan

# definisikan variable metrics
col1, col2, col3 = st.columns(3)

# Menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") # naik dengan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") # naik tapi buruk
col3.metric (label="Pelanggan", value=100, delta=10, delta_color="off") # netral (tidak baik, tidak buruk)

# Menampilkan metric tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) # kosong # naik baik karna disetting default
st.metric("Trees", "91456", "-1132649")

# fungsi write() sebagai superfungsi
df = pd.DataFrame(
np.random.randn(30, 10),
columns=('col_no %d' % i for i in range(10)))
# mendefinisikan beberapa argumen yang ada di fungsi write
st.write("ini adalah data kita", df, "data is in dataframe format.\n", "\nWrite is super function")

# Mendefinisikan random value untuk Chart
df = pd.DataFrame(
np.random.randn(10, 2),
columns= ['a', 'b'])
# Mendefinisikan chart
chart = alt.Chart(df).mark_bar().encode(
x= 'a', y='b', tooltip=['a', 'b'])
# Mendefinisikan chart di dalam fungsi write()
st.write(chart)

# Macig adalah fitur unik untuk menambahkan elemen teks atau kode tanpa fungsi ekplisit seperti st.write()

# Menghitung matematika dengan tidak mendefinisikan fungsi
"menambahkan 5 & 4", 5+4
# Menampilkan variable "a" dan valuenya
a = 5
'a', a

# Menulis markdown menggunakan magic
"""
# Magic Faeture
Markdown working without defining its function explicity.
"""

# Dataframe using magic
df = pd.DataFrame({'col1': [1,2]})
'dataframe', df

# Magic working on chart
import matplotlib.pyplot as plt
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
# Magic Chart
"chart", chart
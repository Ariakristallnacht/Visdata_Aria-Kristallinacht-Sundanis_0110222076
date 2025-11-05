# import library yang dibutuhkan
import streamlit as st

# Bagian 1: text element
# header - untuk membuat tulisan haeder
st.header("ini header") # untuk membuat heardet
st.subheader("ini sub header") # untuk membuat subjudul yang lebih kecil
st.text("ini teks biasa tanpa format") # untuk membuat teks polos tanpa  format
st.markdown("**ini teks bold** dan *ini teks italic*") # mardown untuk memformat teks tebal/miring
st.markdown("""
- ini baris 1
- ini menggunakan markdown multibaris
1. ini baris 2
2. ini menggunakan markdown multibaris
* ini baris 3
* ini menggunakan mardown mutibaris
""")
st.caption("ini caption") # teks kecil dibawah elemen (untuk menjelaskan)

# coba mandiri
# tuliskan:
# 1. Judul praktikum pakai title()
# 2. bagian praktikum pakai subheader()
# 3. nama lengkap anggota - nim pakai markdown multibaris"""

st.title("Praktikum 01 Visualisasi Data")
st.subheader("Bagian 1-text-elements")
st.markdown("""
KELOMPOK 16
- ARIA KRISTALLINACHT SUNDANIS - 0110222076
- BAGUS ACHMAD HIDAYAT - 0110222002
- AZRIL PUTRA SYAHRI - 0110222197
""")

# Bagian 2: Memanpilkan Rumus (LaTeX)
st.header("Displaying LaTeX")
st.latex(r'''\cos^2\thate = 1-2\sin^2\theta''') # rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') # rumus kuadrat binominimal

# Bagian 3: Menampilkan Kode Program
st.header("Displaying Code")
st.subheader("Python Code")

# Simpan ke variable
code = '''
def hello():
    print("Hello, Streamlit!")
'''

# st.code() untuk menampilkan potongna kdoe denga format rapi dan syntax highlighting
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
    public class GFG {
        public static voin main(String arg[]) {
            system.out.printIn("Hello World!")
        }
    }
""", language='java')

# Fungsi st.code () bisa digunakan bahasa pemrogaman lain seperti java, javascript, c++, dll

st.subheader("JavaScript Code")
st.code("""
<p id="demo"></p>
<script>
try {
    addalert("Welcome guest!"); // kesalahan ketik (addalert) sengaja dibuat untuk menimbulkan error
}
catch(err) {
        document.getElementById("demo").innerHTML = err.message; // menampilkan pesan error di elemen HTML dengan id 'demo'
}
</script>
""", language='javascript')
# Kode ini menunjukan baigaimana menangani error (excaption) di javascript
# Hasilnya tidaj dijalankan di streamlit, tapi ditampilkan sebagai contooh kode
import streamlit as st

# Background dengan contain dan overlay
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                      url("https://img.freepik.com/free-photo/top-view-healthy-food-high-protein_23-2148761359.jpg");
    background-size: contain;
    background-position: center top;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Judul dengan teks 'PROTEIN' warna merah
st.markdown(
    "<h1 style='text-align: center; color:white;'>BERAPA SIH KEBUTUHAN <span style='color: red;'>PROTEIN</span>

st.markdown("<h1 style='text-align: center; color: red;'>👋Halloo Sobat Pangan👋 </h1>", unsafe_allow_html=True)

st.write("Yuk Cari Tahu Berapa Banyak Sih Kebutuhan _Protein_ harian kamu? 🤔")

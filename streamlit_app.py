import streamlit as st

# CSS untuk mengganti background Streamlit
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/free-photo/top-view-healthy-food-high-protein_23-2148761359.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Judul dengan teks 'PROTEIN' berwarna merah
st.markdown(
    "<h1 style='text-align: center; color:white;'>BERAPA SIH KEBUTUHAN <span style='color: red;'>PROTEIN</span> HARIAN MU???</h1>",
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: red;'>👋Halloo Sobat Pangan👋 </h1>", unsafe_allow_html=True)

st.write("Yuk Cari Tahu Berapa Banyak Sih Kebutuhan _Protein_ harian kamu? 🤔")

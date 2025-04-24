import streamlit as st
import base64

# Fungsi untuk mengatur background dari gambar lokal
def set_background(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    css = f'''
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
                          url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center top;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)

# Ganti dengan nama file gambar yang kamu upload
set_background("/mnt/data/healthy-fresh-pet-food-ingredients-dark-surface.jpg")

# Judul halaman
st.markdown(
    "<h1 style='text-align: center; color:white;'>BERAPA SIH KEBUTUHAN <span style='color: red;'>PROTEIN</span> HARIAN MU???</h1>",
    unsafe_allow_html=True
)


st.markdown("<h1 style='text-align: center; color: red;'>👋Halloo Sobat Pangan👋 </h1>", unsafe_allow_html=True)

st.write("Yuk Cari Tahu Berapa Banyak Sih Kebutuhan _Protein_ harian kamu? 🤔")

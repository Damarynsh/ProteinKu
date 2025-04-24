import streamlit as st

# Menyisipkan CSS untuk mengganti background
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://img.freepik.com/free-photo/healthy-fresh-pet-food-ingredients-dark-surface_1150-42089.jpg?t=st=1745509027~exp=1745512627~hmac=6dac757c01ffc1963af4755b696cdd5e1cd387be5d48145c3fdd54092468eff3&w=996');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Konten aplikasi Streamlit
st.title("Aplikasi dengan Background Gambar Protein")
st.write("Ini adalah aplikasi Streamlit dengan background gambar protein.")

# Judul halaman
st.markdown(
    "<h1 style='text-align: center; color:white;'>BERAPA SIH KEBUTUHAN <span style='color: red;'>PROTEIN</span> HARIAN MU???</h1>",
    unsafe_allow_html=True
)


st.markdown("<h1 style='text-align: center; color: red;'>👋Halloo Sobat Pangan👋 </h1>", unsafe_allow_html=True)

st.write("Yuk Cari Tahu Berapa Banyak Sih Kebutuhan _Protein_ harian kamu? 🤔")


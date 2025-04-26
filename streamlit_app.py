
import streamlit as st

# CSS untuk background dengan overlay gelap
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),
                    url('https://img.freepik.com/free-photo/healthy-fresh-pet-food-ingredients-dark-surface_1150-42089.jpg?t=st=1745509027~exp=1745512627~hmac=6dac757c01ffc1963af4755b696cdd5e1cd387be5d48145c3fdd54092468eff3&w=996');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
import streamlit as st

st.title("💪 Kalkulator Kebutuhan Protein Harian (Kemenkes Indonesia)")

with st.form("protein_form"):
    st.subheader("Masukkan Data Diri Kamu:")

    gender = st.selectbox("Jenis Kelamin", ("Laki-laki", "Perempuan"))
    age = st.number_input("Umur (tahun)", min_value=0, max_value=120, value=25)
    height = st.number_input("Tinggi Badan (cm)", min_value=0, max_value=250, value=170)
    weight = st.number_input("Berat Badan (kg)", min_value=0.0, max_value=200.0, value=60.0)
    
    tujuan = st.selectbox("Tujuan Fitness Kamu", ("Menurunkan berat badan", "Menjaga berat badan", "Meningkatkan massa otot"))

    submit = st.form_submit_button("Hitung Kebutuhan Protein")

if submit:
    # Menentukan kebutuhan protein berdasarkan jenis kelamin dan usia (referensi Kemenkes)
    if age >= 60:
        kebutuhan_protein = weight * 1.0  # 1.0g per kg berat badan untuk lansia
    else:
        kebutuhan_protein = weight * 0.8  # 0.8g per kg berat badan untuk dewasa

    st.success(f"🎯 Kebutuhan protein harian kamu adalah {kebutuhan_protein:.1f} gram.")

    st.subheader("🍽️ Rekomendasi Makanan untuk Memenuhi Protein Harian")

    # Daftar makanan dan kandungan protein per porsi
    makanan = {
        "Ayam Dada (100g)": 30,
        "Telur (1 butir)": 6,
        "Tempe (100g)": 19,
        "Tahu (100g)": 8,
        "Greek Yogurt (100g)": 10,
        "Ikan Salmon (100g)": 22,
        "Daging Sapi (100g)": 26,
        "Almond (28g)": 6,
        "Kacang Edamame (100g)": 11,
        "Kacang Hitam (100g)": 8,
        "Keju Cottage (100g)": 11
    }

    for makanan_item, protein_per_porsi in makanan.items():
        jumlah_porsi = kebutuhan_protein / protein_per_porsi
        st.write(f"- {makanan_item}: {jumlah_porsi:.1f} porsi")

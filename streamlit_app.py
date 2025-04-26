
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

st.title("💪 Kalkulator Kebutuhan Protein Harian")

with st.form("protein_form"):
    st.subheader("Masukkan Data Diri Kamu:")

    gender = st.selectbox("Jenis Kelamin", ("Laki-laki", "Perempuan"))
    age = st.number_input("Umur (tahun)", min_value=0, max_value=120, value=25)
    height = st.number_input("Tinggi Badan (cm)", min_value=0, max_value=250, value=170)
    weight = st.number_input("Berat Badan (kg)", min_value=0.0, max_value=200.0, value=60.0)
    
    tujuan = st.selectbox("Tujuan Fitness Kamu", ("Menurunkan berat badan", "Menjaga berat badan", "Meningkatkan massa otot"))

    submit = st.form_submit_button("Hitung Kebutuhan Protein")

if submit:
    if gender == "Laki-laki":
        base_protein = 1.2
    else:
        base_protein = 1.0

    if tujuan == "Menurunkan berat badan":
        faktor = 1.2
    elif tujuan == "Menjaga berat badan":
        faktor = 1.5
    else:
        faktor = 1.8

    kebutuhan_protein = weight * base_protein * faktor

    st.success(f"🎯 Kebutuhan protein harian kamu sekitar {kebutuhan_protein:.1f} gram per hari.")

    # Rekomendasi makanan per porsi harian yang dibutuhkan
    st.subheader("🍽️ Rekomendasi Makanan untuk Memenuhi Protein Harian")

    # Protein per porsi makanan
    makanan = {
        "Ayam Dada (100g)": 30,  # protein per 100g
        "Telur (1 butir)": 6,     # protein per butir
        "Tempe (100g)": 19,       # protein per 100g
        "Tahu (100g)": 8,         # protein per 100g
        "Greek Yogurt (100g)": 10, # protein per 100g
        "Ikan Salmon (100g)": 22,  # protein per 100g
        "Daging Sapi (100g)": 26,  # protein per 100g
        "Almond (28g)": 6,         # protein per 28g
        "Kacang Edamame (100g)": 11,  # protein per 100g
        "Kacang Hitam (100g)": 8,    # protein per 100g
        "Keju Cottage (100g)": 11    # protein per 100g
    }

    rekomendasi = []
    
    for makanan_item, protein_per_porsi in makanan.items():
        jumlah_porsi = kebutuhan_protein / protein_per_porsi
        rekomendasi.append(f"{makanan_item}: {jumlah_porsi:.1f} porsi")

    # Tampilkan rekomendasi makanan
    st.write("\n".join(rekomendasi))

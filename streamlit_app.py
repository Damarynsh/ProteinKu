
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

st.title("💪 Kalkulator Kebutuhan Protein Harian (Dengan Kombinasi Makanan)")

with st.form("protein_form"):
    st.subheader("Masukkan Data Diri Kamu:")

    gender = st.selectbox("Jenis Kelamin", ("Laki-laki", "Perempuan"))
    age = st.number_input("Umur (tahun)", min_value=0, max_value=120, value=25)
    height = st.number_input("Tinggi Badan (cm)", min_value=0, max_value=250, value=170)
    weight = st.number_input("Berat Badan (kg)", min_value=0.0, max_value=200.0, value=60.0)

    tujuan = st.selectbox(
        "Apa Tujuan Fitness Kamu?",
        ("Menurunkan berat badan", "Menjaga berat badan", "Meningkatkan massa otot")
    )

    st.subheader("🍽️ Pilih Makanan Favorit Kamu (bisa lebih dari satu)")
    makanan_tersedia = {
        "Ayam Dada": 30,
        "Telur": 13,
        "Tempe": 19,
        "Tahu": 8,
        "Greek Yogurt": 10,
        "Ikan Salmon": 22,
        "Daging Sapi": 26,
        "Almond": 21,
        "Kacang Edamame": 11,
        "Kacang Hitam": 8,
        "Keju Cottage": 11
    }
    pilihan_makanan = st.multiselect("Pilih Makanan:", list(makanan_tersedia.keys()), default=["Tempe", "Telur"])

    submit = st.form_submit_button("Hitung Kebutuhan Protein")

if submit:
    if len(pilihan_makanan) == 0:
        st.error("⚠️ Pilih minimal 1 makanan dulu ya!")
    else:
        # Hitung kebutuhan protein
        if age >= 60:
            kebutuhan_protein = weight * 1.0
        else:
            if tujuan == "Menurunkan berat badan":
                kebutuhan_protein = weight * 1.2
            elif tujuan == "Menjaga berat badan":
                kebutuhan_protein = weight * 0.8
            elif tujuan == "Meningkatkan massa otot":
                kebutuhan_protein = weight * 1.6

        st.success(f"🎯 Kebutuhan protein harian kamu adalah {kebutuhan_protein:.1f} gram.")

        st.subheader("📋 Rekomendasi Konsumsi Harianmu:")

        # Bagi kebutuhan protein secara merata ke pilihan makanan
        kebutuhan_per_makanan = kebutuhan_protein / len(pilihan_makanan)

        for makanan_item in pilihan_makanan:
            protein_per_100g = makanan_tersedia[makanan_item]
            gram_diperlukan = (kebutuhan_per_makanan / protein_per_100g) * 100
            st.write(f"- {makanan_item}: {gram_diperlukan:.0f} gram per hari")

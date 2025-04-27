import streamlit as st
import time
import random

# --- CONFIG HALAMAN ---
st.set_page_config(page_title="Kalkulator Protein Harian", page_icon="🍗", layout="centered")

# --- CSS untuk Background, Tombol, dan Footer ---
st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),
                    url('https://img.freepik.com/free-photo/healthy-fresh-pet-food-ingredients-dark-surface_1150-42089.jpg?t=st=1745509027~exp=1745512627~hmac=6dac757c01ffc1963af4755b696cdd5e1cd387be5d48145c3fdd54092468eff3&w=996');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
    }

    /* Tombol */
    div.stButton > button {
        color: white;
        background-color: #FF6B6B;
        border: none;
        border-radius: 12px;
        padding: 0.75em 2em;
        font-size: 1.2em;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #FF4F4F;
        transform: scale(1.05);
    }

    /* Footer */
    .footer {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        color: white;
        font-size: 0.9em;
        font-weight: bold;
        text-align: center;
        z-index: 9999;
        background-color: rgba(0, 0, 0, 0.6);
        padding: 10px;
        width: 100%;
    }

    /* Card Styling */
    .card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease-in-out;
    }

    /* Styling for each meal box */
    .meal-box {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Text Styling for header and recommendation */
    h3, h4 {
        text-align: center;
    }

    .watermark img {
        width: 20px;
        vertical-align: middle;
        margin-left: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- DATA MAKANAN ---
makanan_tersedia = {
    "Ayam": {"protein_per_100g": 27, "satuan": "gram", "icon": "🍗"},
    "Daging sapi": {"protein_per_100g": 26, "satuan": "gram", "icon": "🥩"},
    "Ikan salmon": {"protein_per_100g": 25, "satuan": "gram", "icon": "🐟"},
    "Ikan tuna": {"protein_per_100g": 23, "satuan": "gram", "icon": "🐟"},
    "Tempe": {"protein_per_100g": 20, "satuan": "gram", "icon": "🍽️"},
    "Tahu": {"protein_per_100g": 8, "satuan": "gram", "icon": "🍽️"},
    "Telur": {"protein_per_butir": 6.5, "satuan": "butir", "icon": "🥚"},
    "Brokoli": {"protein_per_100g": 2.8, "satuan": "gram", "icon": "🥦"},
    "Kacang tanah": {"protein_per_100g": 25, "satuan": "gram", "icon": "🥜"},
    "Oat": {"protein_per_100g": 16.9, "satuan": "gram", "icon": "🌾"},
}

# --- FUNGSI HALAMAN ---
def halaman_awal():
    st.title("🥩Seberapa banyak kebutuhan protein harian ku?")
    st.subheader("Halo sobat pangan!!!")
    st.write("""
    Protein adalah nutrisi penting untuk membangun dan memperbaiki jaringan tubuh, 
    termasuk otot, kulit, dan enzim. Mengonsumsi cukup protein membantu menjaga kesehatan tubuh, 
    meningkatkan metabolisme, dan mendukung proses penyembuhan. Yuk, cari tahu berapa banyak protein yang kamu butuhkan setiap harinya!
    """)
    
    if st.button("Mulai Hitung ➡️"):
        st.session_state.halaman = "kalkulator"
        st.rerun()

def kalkulator():
    st.title("Kalkulator Kebutuhan Protein Harian")

    gender = st.selectbox("Jenis Kelamin:", ["Pria", "Wanita"])
    age = st.number_input("Umur (tahun):", min_value=1, max_value=120)
    height = st.number_input("Tinggi Badan (cm):", min_value=50, max_value=250)
    weight = st.number_input("Berat Badan (kg):", min_value=10, max_value=300)
    tujuan = st.selectbox("Tujuan kamu:", ["Menurunkan berat badan", "Menjaga berat badan", "Meningkatkan massa otot"])
    jumlah_makan = st.selectbox("Berapa kali makan per hari?", [2, 3, 4, 5])

    pilihan_makanan = st.multiselect(
        "Pilih makanan yang kamu sukai:",
        list(makanan_tersedia.keys()),
        default=["Ayam", "Tempe", "Telur"]
    )

    if st.button("Hitung Kebutuhan Protein 🍽️"):
        st.session_state.gender = gender
        st.session_state.age = age
        st.session_state.height = height
        st.session_state.weight = weight
        st.session_state.tujuan = tujuan
        st.session_state.jumlah_makan = jumlah_makan
        st.session_state.pilihan_makanan = pilihan_makanan
        loading_screen()

def loading_screen():
    progress_text = "Tunggu ya, kita hitung dulu kebutuhan proteinmu..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.06)
        my_bar.progress(percent_complete + 1, text=progress_text)

    st.session_state.halaman = "hasil"
    st.rerun()

def hasil_kalkulator():
    st.title("🔥Hasil Kebutuhan Proteinmu🔥")

    weight = st.session_state.weight
    tujuan = st.session_state.tujuan
    jumlah_makan = st.session_state.jumlah_makan
    pilihan_makanan = st.session_state.pilihan_makanan
    age = st.session_state.age

    # Kalkulasi kebutuhan protein berdasarkan standar Kemenkes
    if age >= 60:
        kebutuhan_protein = weight * 1.0
    else:
        if tujuan == "Menurunkan berat badan":
            kebutuhan_protein = weight * 1.2
        elif tujuan == "Menjaga berat badan":
            kebutuhan_protein = weight * 0.8
        else:
            kebutuhan_protein = weight * 1.6

    kebutuhan_per_makan = kebutuhan_protein / jumlah_makan

    st.markdown(f"<h2 style='text-align: center;'>✨ Kamu membutuhkan {kebutuhan_protein:.1f} gram protein setiap hari! ✨</h2>", unsafe_allow_html=True)
    st.write("---")

    st.subheader("Tips Konsumsi Harian:")

    for i in range(1, jumlah_makan + 1):
        # Start meal box
        with st.container():
            st.markdown('<div class="meal-box">', unsafe_allow_html=True)
            st.write(f"### 🍽️ Makan ke-{i}:")

            kebutuhan_sesi = kebutuhan_per_makan
            makanan_dipakai = random.sample(pilihan_makanan, min(2, len(pilihan_makanan)))
            kebutuhan_per_makanan = kebutuhan_sesi / len(makanan_dipakai)

            rekomendasi = []
            for makanan_item in makanan_dipakai:
                data = makanan_tersedia[makanan_item]
                satuan = data["satuan"]
                icon = data["icon"]

                if makanan_item == "Telur":
                    protein_per_butir = 6.5
                    butir_diperlukan = kebutuhan_per_makanan / protein_per_butir
                    rekomendasi.append(f"{icon} {butir_diperlukan:.1f} butir {makanan_item}")
                else:
                    protein_per_100g = data["protein_per_100g"]
                    gram_diperlukan = (kebutuhan_per_makanan / protein_per_100g) * 100
                    rekomendasi.append(f"{icon} {gram_diperlukan:.0f} gram {makanan_item}")

            st.write(", ".join(rekomendasi))

            # End meal box
            st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    if st.button("🔙 Kembali ke Kalkulator"):
        st.session_state.halaman = "kalkulator"
        st.rerun()

# --- LOGIC NAVIGASI HALAMAN ---
if "halaman" not in st.session_state:
    st.session_state.halaman = "awal"

if st.session_state.halaman == "awal":
    halaman_awal()
elif st.session_state.halaman == "kalkulator":
    kalkulator()
elif st.session_state.halaman == "hasil":
    hasil_kalkulator()

# Footer Watermark
st.markdown(
    """
    <div class="footer">
        © 2025 POLITEKNIK AKA BOGOR - D3 Penjaminan Mutu Industri Pangan.
    </div>
    """,
    unsafe_allow_html=True
)

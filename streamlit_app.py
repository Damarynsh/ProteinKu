import streamlit as st
import time
import random

# --- WAJIB: Set Page Config PALING ATAS ---
st.set_page_config(page_title="Kalkulator Protein Harian", page_icon="🍗", layout="centered")

# --- Background CSS ---
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
    button {
        background-color: #f63366;
        color: white;
        border: none;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        border-radius: 12px;
        transition: background-color 0.3s;
    }
    button:hover {
        background-color: #e6004c;
    }
    h1, h2, h3 {
        color: #ffb703;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- DATA MAKANAN ---
makanan_tersedia = {
    "Ayam Dada": {"protein_per_100g": 30, "satuan": "gram"},
    "Telur": {"protein_per_100g": 13, "satuan": "butir"},  # 6.5g protein per butir
    "Tempe": {"protein_per_100g": 19, "satuan": "gram"},
    "Tahu": {"protein_per_100g": 8, "satuan": "gram"},
    "Greek Yogurt": {"protein_per_100g": 10, "satuan": "gram"},
    "Ikan Salmon": {"protein_per_100g": 22, "satuan": "gram"},
    "Ikan Tuna": {"protein_per_100g": 23, "satuan": "gram"},
    "Daging Sapi": {"protein_per_100g": 26, "satuan": "gram"},
    "Almond": {"protein_per_100g": 21, "satuan": "gram"},
    "Kacang Edamame": {"protein_per_100g": 11, "satuan": "gram"},
    "Kacang Hitam": {"protein_per_100g": 8, "satuan": "gram"},
    "Kacang Tanah": {"protein_per_100g": 25, "satuan": "gram"},
    "Keju Cottage": {"protein_per_100g": 11, "satuan": "gram"},
    "Brokoli": {"protein_per_100g": 2.8, "satuan": "gram"},
    "Oat": {"protein_per_100g": 13, "satuan": "gram"}
}

# --- FUNGSI HALAMAN AWAL ---
def halaman_awal():
    st.title("Seberapa banyak kebutuhan protein harian ku?")
    st.subheader("Halo sobat pangan! 👋")
    st.markdown("""
    Protein adalah salah satu zat gizi makro yang sangat penting untuk kesehatan tubuh manusia.  
    Tubuh kita membutuhkan protein untuk membangun dan memperbaiki jaringan, termasuk otot, kulit, dan organ-organ vital.  
    Protein juga berperan dalam pembentukan enzim, hormon, serta mendukung sistem kekebalan tubuh.  
    Asupan protein yang cukup membantu menjaga massa otot, mendukung pertumbuhan, serta mempercepat pemulihan setelah aktivitas fisik.
    """)
    
    if st.button("Mulai Kalkulator ➡️", use_container_width=True):
        st.session_state.halaman = "kalkulator"

# --- FUNGSI KALKULATOR ---
def kalkulator_protein():
    st.title("💪 Kalkulator Kebutuhan Protein Harian")

    with st.form("form_protein"):
        st.subheader("Masukkan Data Diri Kamu:")
        gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        age = st.number_input("Umur (tahun)", min_value=0, max_value=120, value=25)
        height = st.number_input("Tinggi Badan (cm)", min_value=0, max_value=250, value=170)
        weight = st.number_input("Berat Badan (kg)", min_value=0.0, max_value=200.0, value=60.0)

        tujuan = st.selectbox(
            "Apa Tujuan Fitness Kamu?",
            ["Menurunkan berat badan", "Menjaga berat badan", "Meningkatkan massa otot"]
        )

        jumlah_makan = st.number_input("Mau makan berapa kali sehari?", min_value=2, max_value=8, value=3)

        pilihan_makanan = st.multiselect(
            "🍽️ Pilih Makanan Favorit (bisa lebih dari satu)", 
            list(makanan_tersedia.keys()), 
            default=["Tempe", "Telur", "Ikan Salmon", "Tahu", "Kacang Tanah"]
        )

        submit = st.form_submit_button("Hitung Kebutuhan Protein")

    if submit:
        if not pilihan_makanan:
            st.error("⚠️ Pilih minimal 1 makanan dulu ya!")
            return
        
        # Simpan semua input ke session_state
        st.session_state.gender = gender
        st.session_state.age = age
        st.session_state.height = height
        st.session_state.weight = weight
        st.session_state.tujuan = tujuan
        st.session_state.jumlah_makan = jumlah_makan
        st.session_state.pilihan_makanan = pilihan_makanan

        st.session_state.halaman = "loading"

# --- FUNGSI LOADING SCREEN ---
def loading_screen():
    with st.spinner("Tunggu ya, kita hitung dulu kebutuhan proteinmu..."):
        time.sleep(3)  # durasi loading
    st.session_state.halaman = "hasil"

# --- FUNGSI MENAMPILKAN HASIL ---
def hasil_kalkulator():
    st.title("🎯 Hasil Kebutuhan Protein Kamu")

    weight = st.session_state.weight
    tujuan = st.session_state.tujuan
    jumlah_makan = st.session_state.jumlah_makan
    pilihan_makanan = st.session_state.pilihan_makanan

    # Kalkulasi kebutuhan protein
    if st.session_state.age >= 60:
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
        st.write(f"### 🍽️ Makan ke-{i}:")
        kebutuhan_sesi = kebutuhan_per_makan

        makanan_dipakai = random.sample(pilihan_makanan, min(2, len(pilihan_makanan)))
        kebutuhan_per_makanan = kebutuhan_sesi / len(makanan_dipakai)

        rekomendasi = []
        for makanan_item in makanan_dipakai:
            data = makanan_tersedia[makanan_item]
            satuan = data["satuan"]

            if makanan_item == "Telur":
                protein_per_butir = 6.5
                butir_diperlukan = kebutuhan_per_makanan / protein_per_butir
                rekomendasi.append(f"{butir_diperlukan:.1f} butir {makanan_item}")
            else:
                protein_per_100g = data["protein_per_100g"]
                gram_diperlukan = (kebutuhan_per_makanan / protein_per_100g) * 100
                rekomendasi.append(f"{gram_diperlukan:.0f} gram {makanan_item}")

        st.write(", ".join(rekomendasi))

# --- LOGIKA HALAMAN ---
if 'halaman' not in st.session_state:
    st.session_state.halaman = "awal"

if st.session_state.halaman == "awal":
    halaman_awal()
elif st.session_state.halaman == "kalkulator":
    kalkulator_protein()
elif st.session_state.halaman == "loading":
    loading_screen()
elif st.session_state.halaman == "hasil":
    hasil_kalkulator()

import streamlit as st
import time
import random

# --- CONFIG HALAMAN ---
st.set_page_config(page_title="Kalkulator Protein Harian", page_icon="🍗", layout="centered")

# --- CSS (Tetap sama) ---
st.markdown(
    """
    <style>
    body, h1, h2, h3, h4, h5, h6, p, span, label, div, li, ul, ol, select, input, textarea, button {
        color: white !important;
    }
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),
                    url('https://img.freepik.com/free-photo/healthy-fresh-pet-food-ingredients-dark-surface_1150-42089.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
    }
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
    .meal-box {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h3, h4 {
        text-align: center;
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
    Protein adalah nutrisi penting untuk membangun dan memperbaiki jaringan tubuh. Yuk, cari tahu berapa banyak protein yang kamu butuhkan setiap harinya!
    """)
    st.image("https://cdn-icons-png.flaticon.com/512/1046/1046784.png", width=100)

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

def hasil_kalkulator():
    st.title("🔥Hasil Kebutuhan Protein Kamu")

    weight = st.session_state.weight
    tujuan = st.session_state.tujuan
    jumlah_makan = st.session_state.jumlah_makan
    pilihan_makanan = st.session_state.pilihan_makanan
    age = st.session_state.age

    if age >= 60:
        kebutuhan_protein = weight * 1.0
    else:
        kebutuhan_protein = weight * {"Menurunkan berat badan": 1.2, "Menjaga berat badan": 0.8, "Meningkatkan massa otot": 1.6}[tujuan]

    kebutuhan_per_makan = kebutuhan_protein / jumlah_makan
    st.markdown(f"<h2 style='text-align: center;'>✨ Kamu membutuhkan {kebutuhan_protein:.1f} gram protein setiap hari! ✨</h2>", unsafe_allow_html=True)

    st.subheader("Tips Konsumsi Harian:")

    for i in range(1, jumlah_makan + 1):
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
                    butir_diperlukan = kebutuhan_per_makanan / 6.5
                    rekomendasi.append(f"{icon} {butir_diperlukan:.1f} butir {makanan_item}")
                else:
                    gram_diperlukan = (kebutuhan_per_makanan / data["protein_per_100g"]) * 100
                    rekomendasi.append(f"{icon} {gram_diperlukan:.0f} gram {makanan_item}")

            st.write(", ".join(rekomendasi))
            st.markdown('</div>', unsafe_allow_html=True)

def halaman_tentang():
    st.title("Tentang Website Ini")
    st.write("""
    Website ini dibuat untuk membantu masyarakat Indonesia dalam menghitung kebutuhan protein harian mereka berdasarkan usia, berat badan, dan tujuan kesehatan masing-masing.
    
    Dengan fitur kalkulator yang praktis serta rekomendasi makanan bergizi, website ini diharapkan dapat membantu pengguna untuk lebih peduli terhadap kecukupan protein dalam pola makan sehari-hari.

    Dibuat oleh mahasiswa D3 Penjaminan Mutu Industri Pangan, POLITEKNIK AKA BOGOR.
    """)

# --- FUNGSI LOADING ---
def loading_screen():
    progress_text = "Tunggu ya, kita hitung dulu kebutuhan proteinmu..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.03)
        my_bar.progress(percent_complete + 1, text=progress_text)
    st.session_state.halaman = "hasil"
    st.rerun()

# --- SIDEBAR MENU ---
halaman_pilihan = st.sidebar.radio("Navigasi", ["Beranda", "Kalkulator", "Tentang"])

# --- RENDER SESUAI PILIHAN ---
if halaman_pilihan == "Beranda":
    halaman_awal()
elif halaman_pilihan == "Kalkulator":
    if "halaman" in st.session_state and st.session_state.halaman == "hasil":
        hasil_kalkulator()
    else:
        kalkulator()
elif halaman_pilihan == "Tentang":
    halaman_tentang()

# --- FOOTER ---
st.markdown(
    """
    <div class="footer">
        © 2025 POLITEKNIK AKA BOGOR - D3 Penjaminan Mutu Industri Pangan.
    </div>
    """,
    unsafe_allow_html=True
)

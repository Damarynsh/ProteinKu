import streamlit as st
import time
import random

#BUAT CONFIG NAMA WEB BIAR KEREN
st.set_page_config(page_title="Kalkulator Protein Harian", page_icon="🍗", layout="centered")

st.markdown("""
    <style>
        /* Styling untuk selectbox */
        div[data-baseweb="select"] > div {
            background-color: #333333;
            color: white;
        }

        div[data-baseweb="select"] div[role="combobox"] {
            background-color: #333333 !important;
            color: white !important;
        }

        div[data-baseweb="select"] div[role="option"] {
            background-color: #333333 !important;
            color: white !important;
        }

        div[data-baseweb="menu"] {
            background-color: #333333 !important;
            color: white !important;
        }

        div[data-baseweb="option"]:hover {
            background-color: #444444 !important;
        }

        /* Styling untuk number_input */
        input[type="number"] {
            background-color: #333333;
            color: white;
            border: 1px solid #555555;
            padding: 0.5em;
            border-radius: 5px;
        }

        /* Styling label teks */
        label {
            color: white;
        }

        /* Styling untuk latar belakang umum aplikasi */
        .stApp {
            background-color: #1e1e1e;
        }
    </style>
""", unsafe_allow_html=True)


#CODING BUAT BACKGROUND, FONT, BUTTON
st.markdown(
    """
    <style>
    body, h1, h2, h3, h4, h5, h6, p, span, label, div, li, ul, ol, select, input, textarea, button {
        color: white !important;
    }

    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)),
                    url('https://img.freepik.com/free-photo/healthy-fresh-pet-food-ingredients-dark-surface_1150-42089.jpg?t=st=1745509027~exp=1745512627~hmac=6dac757c01ffc1963af4755b696cdd5e1cd387be5d48145c3fdd54092468eff3&w=996');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
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
    /* Ubah warna background sidebar */
section[data-testid="stSidebar"] {
    background-color: #1c1c1c;
    color: white;
}

/* Ubah warna teks sidebar */
section[data-testid="stSidebar"] .css-1v0mbdj, 
section[data-testid="stSidebar"] .css-10trblm, 
section[data-testid="stSidebar"] .css-1y4p8pa, 
section[data-testid="stSidebar"] label {
    color: white !important;
}

    </style>
    """,
    unsafe_allow_html=True
)

# INI DATA LIST MAKANAN
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

# --- HALAMAN BERANDA AWAL NO 1 ---
def halaman_awal():
    st.markdown("<h1 style='text-align: center;'>🥩</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Selamat Datang di Kalkulator Protein Harian</h2>", unsafe_allow_html=True)
    st.write("---")

    st.markdown("""
    ### Apa itu Protein?
    Protein adalah molekul besar yang terdiri dari asam amino dan sangat penting bagi tubuh manusia. 
    Protein berperan sebagai bahan pembangun utama jaringan tubuh seperti otot, kulit, dan organ dalam.

    ### Kegunaan Protein
    - Membantu membentuk dan memperbaiki jaringan tubuh
    - Membuat enzim, hormon, dan senyawa kimia penting lainnya
    - Menyediakan energi saat tubuh kekurangan karbohidrat dan lemak

    ### Manfaat Protein bagi Tubuh
    - **Meningkatkan massa otot**: Membantu pertumbuhan dan pemeliharaan otot, terutama saat berolahraga
    - **Menjaga berat badan ideal**: Membuat kenyang lebih lama dan membantu pembakaran lemak
    - **Mendukung kesehatan tulang**: Protein berkaitan dengan kekuatan tulang dan mencegah osteoporosis
    - **Mempercepat proses pemulihan**: Membantu penyembuhan luka dan cedera

    ---
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>Yuk cari tahu berapa banyak kebutuhan protein harianmu! 👇</h4>", unsafe_allow_html=True)

    if st.button("🔥Mulai Hitung Sekarang"):
        st.session_state.halaman = "Kalkulator"
        st.rerun()


# --- HALAMANN KALKULATOR KEDUA ---
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

    st.session_state.halaman = "Hasil"
    st.rerun()

# --- HASIL KALKULATOR NYA HEHE ---
def hasil_kalkulator():
    st.markdown("""
    <style>
    .protein-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        text-align: center;
        margin-bottom: 30px;
        color: white;
    }

    .protein-value {
        font-size: 48px;
        font-weight: bold;
        color: #FFD700;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 22px;
        margin-bottom: 5px;
    }

    .meal-card {
        background-color: rgba(255,255,255,0.12);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🎯 Hasil Kebutuhan Protein Kamu")

    # BUAT TUJUAN PILIHANNYA
    weight = st.session_state.weight
    tujuan = st.session_state.tujuan
    jumlah_makan = st.session_state.jumlah_makan
    pilihan_makanan = st.session_state.pilihan_makanan
    age = st.session_state.age

    # SISTEM KALKULATOR TUJUANNYAA
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

    # HASIL PROTEIN JADI SEGEDE GABAN
    st.markdown(f"""
    <div class="protein-box">
        <div class="subtitle">Kebutuhan protein harianmu adalah:</div>
        <div class="protein-value">{kebutuhan_protein:.1f} gram</div>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🍱 Rekomendasi Menu Setiap Waktu Makan:")

    # REFERENSI MADANG FULL PROTEIN
    for i in range(1, jumlah_makan + 1):
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

        st.markdown(f"""
        <div class="meal-card">
            <h4 style="text-align:center;">🍽️ Makan ke-{i}</h4>
            <p style="text-align:center; font-size:18px;">{' + '.join(rekomendasi)}</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    if st.button("🔙 Kembali ke Kalkulator"):
        st.session_state.halaman = "Kalkulator"
        st.rerun()


# --- HALAMAN TENTANG TERAKHIR ---
def halaman_tentang():
    st.markdown("<h1 style='text-align: center;'>📝 Tentang Aplikasi Ini</h1>", unsafe_allow_html=True)
    st.markdown("""
    <ul style='font-size: 18px;'>
        <li>Aplikasi ini dirancang untuk membantu menghitung kebutuhan protein harian pada tubuh manusia.</li>
        <li>Website ini dibuat sebagai bagian dari project dalam mata kuliah Logika Pemograman Komputer mahasiswa D3 Penjaminan Mutu Industri Pangan di POLITEKNIK AKA BOGOR.</li>
        <li>Website yang kami rancang dapat membantu dalam perencanaan makan sehat, terutama untuk yang sedang diet atau membentuk otot.</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; font-size: 20px; font-style: italic; margin-top: 30px;'>
        “Jadikan makanan sehat sebagai kebiasaan, bukan sekadar pilihan.”
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h3 style='margin-top: 40px;'>📚 Sumber Referensi:</h3>
    <ul style='font-size: 17px;'>
        <li>World Health Organization (WHO) – Protein and amino acid requirements in human nutrition.</li>
        <li>Peraturan Menteri Kesehatan Republik Indonesia Nomor 28 Tahun 2019 – Angka Kecukupan Gizi (AKG).</li>
        <li>ESPEN Guidelines on Clinical Nutrition and Aging – European Society for Clinical Nutrition and Metabolism.</li>
        <li>Literatur kebugaran dan nutrisi modern seperti NASM & Precision Nutrition (untuk penyesuaian tujuan).</li>
    </ul>
    """, unsafe_allow_html=True)

# --- INISIALISASI HALAMAN SAAT APLIKASI DIMULAI ---
if "halaman" not in st.session_state:
    st.session_state.halaman = "Beranda"

# --- SIDEBAR NAVIGASI YG DI SISI KIRI ---
def set_halaman_baru():
    st.session_state.halaman = st.session_state.pilihan_sidebar

# CEK INDEX HARUS AMAN
opsi_menu = ["Beranda", "Kalkulator", "Tentang"]
index_awal = opsi_menu.index(st.session_state.halaman) if st.session_state.halaman in opsi_menu else 0

st.sidebar.radio(
    "Navigasi", 
    opsi_menu,
    key="pilihan_sidebar",
    index=index_awal,
    on_change=set_halaman_baru
)

# --- BUTTON HALAMAN BUAT RENDERNYA ---
if st.session_state.halaman == "Beranda":
    halaman_awal()
elif st.session_state.halaman == "Kalkulator":
    kalkulator()
elif st.session_state.halaman == "Hasil":
    hasil_kalkulator()
elif st.session_state.halaman == "Tentang":
    halaman_tentang()

# --- FOOTER BUAT WATERMARK ---
st.markdown(
    """
    <div class="footer">
        © 2025 POLITEKNIK AKA BOGOR - D3 Penjaminan Mutu Industri Pangan.
    </div>
    """,
    unsafe_allow_html=True
)

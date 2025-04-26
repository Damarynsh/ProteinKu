import streamlit as st
import time

# --- Konfigurasi halaman ---
st.set_page_config(page_title="Kalkulator Protein Harian", page_icon="🍗", layout="centered")

# --- CSS untuk Background dan Tombol ---
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
        background-color: #800000; /* Maroon */
        border: none;
        border-radius: 12px;
        padding: 0.75em 2em;
        font-size: 1.2em;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #a52a2a;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- State Awal ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- Fungsi Navigasi ---
def go_to_input():
    st.session_state.page = 'input'

def go_to_result():
    st.session_state.page = 'result'

def go_back_home():
    st.session_state.page = 'home'

# --- Konten Halaman Home ---
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center;'>Seberapa Banyak Kebutuhan Protein Harian Ku?</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Halo sobat pangan!</h3>", unsafe_allow_html=True)
    st.write("""
    Protein adalah salah satu nutrisi makro yang sangat penting bagi tubuh manusia.  
    Protein berperan dalam pembentukan otot, memperbaiki jaringan tubuh, serta memproduksi enzim dan hormon.  
    Kebutuhan protein setiap orang berbeda-beda tergantung usia, jenis kelamin, berat badan, tinggi badan, dan tujuan kebugaran.
    """)
    st.markdown("##")
    st.markdown("##")
    st.markdown(" ")
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("Cek Protein Ku"):
        go_to_input()
    st.markdown("</div>", unsafe_allow_html=True)

# --- Konten Halaman Input ---
elif st.session_state.page == 'input':
    st.header("Masukkan Data Diri Kamu!")

    gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
    age = st.number_input("Umur (tahun)", min_value=0, max_value=100, value=25)
    height = st.number_input("Tinggi Badan (cm)", min_value=0, max_value=250, value=170)
    weight = st.number_input("Berat Badan (kg)", min_value=0, max_value=300, value=65)
    goal = st.selectbox("Tujuan Fitness", ["Menurunkan berat badan", "Menjaga kebugaran", "Meningkatkan massa otot"])
    meals_per_day = st.selectbox("Berapa kali kamu ingin makan per hari?", [2, 3, 4, 5, 6])

    if st.button("Hitung Kebutuhan Protein"):
        with st.spinner('Tunggu ya, kita hitung dulu kebutuhan protein mu...'):
            time.sleep(3)  # simulasi loading
        st.session_state.data = {
            'gender': gender,
            'age': age,
            'height': height,
            'weight': weight,
            'goal': goal,
            'meals_per_day': meals_per_day
        }
        go_to_result()

    st.markdown("##")
    st.button("🔙 Kembali ke Beranda", on_click=go_back_home)

# --- Konten Halaman Result ---
elif st.session_state.page == 'result':
    data = st.session_state.data

    # --- Menghitung kebutuhan protein berdasarkan standar Kemenkes Indonesia ---
    if data['age'] < 65:
        base_protein = 1.0  # gr per kg berat badan untuk dewasa
    else:
        base_protein = 1.2  # gr per kg berat badan untuk lansia

    if data['goal'] == "Menurunkan berat badan":
        multiplier = 1.2
    elif data['goal'] == "Menjaga kebugaran":
        multiplier = 1.5
    else:  # Meningkatkan massa otot
        multiplier = 1.8

    kebutuhan_protein = round(data['weight'] * base_protein * multiplier, 1)

    st.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>Kebutuhan Proteinmu: {kebutuhan_protein} gram/hari</h1>", unsafe_allow_html=True)
    st.write(" ")

    # --- Rekomendasi Makanan ---
    makanan = {
        "Ayam rebus (gram)": 27,
        "Tahu (gram)": 8,
        "Tempe (gram)": 19,
        "Salmon (gram)": 25,
        "Ikan Tuna (gram)": 23,
        "Telur (butir)": 6,
        "Brokoli (gram)": 2.8,
        "Kacang Tanah (gram)": 25,
        "Oat (gram)": 16.9
    }

    st.subheader("Rekomendasi Konsumsi Harian:")

    rekomendasi = {}
    kebutuhan_sisa = kebutuhan_protein

    for makanan_item, protein_per_unit in makanan.items():
        if "Telur" in makanan_item:
            jumlah = kebutuhan_sisa / protein_per_unit
            rekomendasi[makanan_item] = f"{round(jumlah)} butir"
        else:
            jumlah = kebutuhan_sisa / protein_per_unit * 100  # gram
            rekomendasi[makanan_item] = f"{round(jumlah)} gram"

    for makanan_item, jumlah in rekomendasi.items():
        st.write(f"- {makanan_item}: {jumlah}")

    st.markdown("---")

    st.subheader("Tips Konsumsi Protein:")
    st.write(f"Bagi kebutuhan proteinnya ke dalam {data['meals_per_day']} kali makan sehari.")
    protein_per_meal = round(kebutuhan_protein / data['meals_per_day'], 1)
    st.write(f"Setiap makan, usahakan konsumsi sekitar {protein_per_meal} gram protein.")

    st.markdown("##")
    st.button("🔙 Cek Ulang", on_click=go_back_home)

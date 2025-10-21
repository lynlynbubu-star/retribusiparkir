%%writefile app.py
# ======================================================
# Aplikasi AI Dummy - Prediksi Potensi Retribusi Parkir
# Kota Cilegon
# Kelompok 4 - Sistem Informasi, Kampus Cilegon
# ======================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import folium
from streamlit_folium import st_folium

# Konfigurasi halaman
st.set_page_config(page_title="AI Parkir Cilegon", layout="wide")
st.title("🚗 Aplikasi AI Parkir Cilegon")
st.markdown("### Prediksi dan Visualisasi Potensi Retribusi Parkir Menggunakan Kecerdasan Buatan")

# Inisialisasi session_state untuk menyimpan lokasi parkir
if "parkir_locations" not in st.session_state:
    st.session_state.parkir_locations = [
        {"nama": "Alun-Alun Cilegon", "lat": -6.0068, "lon": 106.0491},
        {"nama": "Terminal Cilegon", "lat": -6.0030, "lon": 106.0550},
        {"nama": "Pasar Kranggot", "lat": -6.0125, "lon": 106.0532},
        {"nama": "Stasiun Cilegon", "lat": -6.0152, "lon": 106.0557},
    ]

# Layout dua kolom
col1, col2 = st.columns(2)

# ===============================
# 🧩 BAGIAN 1 - INPUT DATA
# ===============================
with col1:
    st.subheader("1️⃣ Input Data Kendaraan")

    def parse_number(input_text, default_value):
        """Fungsi untuk membaca angka dengan titik/koma."""
        if isinstance(input_text, (int, float)):
            return input_text
        try:
            clean = input_text.replace(".", "").replace(",", "")
            return int(clean)
        except:
            return default_value

    roda_dua_str = st.text_input("Jumlah Kendaraan Roda Dua", value="41.564")
    roda_empat_str = st.text_input("Jumlah Kendaraan Roda Empat", value="13.369")
    tarif_str = st.text_input("Tarif Retribusi per Kendaraan (Rp)", value="2.000")

    roda_dua = parse_number(roda_dua_str, 41564)
    roda_empat = parse_number(roda_empat_str, 13369)
    tarif_retribusi = parse_number(tarif_str, 2000)

    persentase_pembayar = st.slider("Persentase Kendaraan yang Bayar Retribusi (%)", 0, 100, 25)
    parkir_liar = st.slider("Perkiraan Parkir Liar (tidak dikelola Dishub) (%)", 0, 100, 30)

    # Input tanggal
    st.subheader("📅 Pilih Tanggal Proyeksi")
    tanggal_awal = st.date_input("Tanggal Awal", value=datetime.today())
    
    st.info("Masukkan data sesuai kondisi lapangan Kota Cilegon. Gunakan titik (.) atau koma (,) untuk pemisah ribuan.")

# ===============================
# 🧠 BAGIAN 2 - PROSES & VISUALISASI
# ===============================
with col2:
    st.subheader("2️⃣ Hasil Prediksi dan Visualisasi")

    if st.button("🚀 Proses Prediksi"):
        # ===============================
        # PROSES PERHITUNGAN (AI Dummy)
        # ===============================
        total_kendaraan = roda_dua + roda_empat
        kendaraan_bayar = total_kendaraan * (persentase_pembayar / 100)
        potensi_retribusi = kendaraan_bayar * tarif_retribusi
        potensi_hilang = total_kendaraan * (parkir_liar / 100) * tarif_retribusi
        prediksi_naik = potensi_retribusi * 1.05

        # Proyeksi harian, bulanan, tahunan
        potensi_harian = potensi_retribusi
        potensi_bulanan = potensi_harian * 30
        potensi_tahunan = potensi_harian * 365

        # ===============================
        # OUTPUT TEKS
        # ===============================
        st.success(f"💰 **Potensi Retribusi Harian:** Rp {potensi_harian:,.0f}")
        st.info(f"📆 **Potensi Bulanan (30 hari):** Rp {potensi_bulanan:,.0f}")
        st.info(f"📅 **Potensi Tahunan (365 hari):** Rp {potensi_tahunan:,.0f}")
        st.warning(f"🚫 **Potensi Retribusi Hilang (Parkir Liar):** Rp {potensi_hilang:,.0f}")
        st.info(f"📈 **Prediksi AI (kenaikan 5%):** Rp {prediksi_naik:,.0f}")

        # ===============================
        # VISUALISASI DATA BAR
        # ===============================
        data = pd.DataFrame({
            "Kategori": ["Bayar Retribusi", "Parkir Liar"],
            "Nilai (Rp)": [potensi_retribusi, potensi_hilang]
        })

        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(data["Kategori"], data["Nilai (Rp)"], color=["green", "red"])
        ax.set_title("Visualisasi Potensi Pendapatan vs Parkir Liar")
        ax.set_ylabel("Nilai (Rp)")
        st.pyplot(fig)

# ===============================
# 🗺️ BAGIAN 3 - PETA LOKASI DINAMIS
# ===============================
st.subheader("📍 Lokasi Retribusi Parkir di Cilegon")

with st.expander("➕ Tambah Lokasi Baru"):
    nama_lokasi = st.text_input("Nama Lokasi")
    lat_lokasi = st.number_input("Latitude", value=-6.0068, format="%.6f")
    lon_lokasi = st.number_input("Longitude", value=106.0491, format="%.6f")
    
    if st.button("Tambahkan Lokasi"):
        if nama_lokasi:
            st.session_state.parkir_locations.append({
                "nama": nama_lokasi,
                "lat": lat_lokasi,
                "lon": lon_lokasi
            })
            st.success(f"Lokasi '{nama_lokasi}' berhasil ditambahkan!")

# Tampilkan peta dengan semua lokasi
m = folium.Map(location=[-6.006, 106.05], zoom_start=14)
for loc in st.session_state.parkir_locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=loc["nama"],
        icon=folium.Icon(color="blue", icon="parking", prefix="fa")
    ).add_to(m)

st_data = st_folium(m, width=700, height=400)

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("© 2025 Kelompok 4 – Sistem Informasi, Kampus Cilegon | Dibuat dengan ❤️ menggunakan Streamlit")

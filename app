%%writefile app.py
# ======================================================
# Aplikasi Pajak Hotel & Restoran - Kota Cilegon
# Kelompok 4 - Sistem Informasi, Kampus Cilegon
# ======================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import folium
from streamlit_folium import st_folium

# Konfigurasi halaman
st.set_page_config(page_title="Pajak Hotel & Restoran Cilegon", layout="wide")
st.title("🏨 Aplikasi Pajak Hotel & Restoran Cilegon")
st.markdown("### Prediksi dan Visualisasi Potensi Pajak Hotel & Restoran Menggunakan Kecerdasan Buatan")

# Inisialisasi session_state untuk menyimpan lokasi
if "locations" not in st.session_state:
    st.session_state.locations = [
        {"nama": "Hotel Cilegon", "lat": -6.0068, "lon": 106.0491},
        {"nama": "Restoran Kranggot", "lat": -6.0125, "lon": 106.0532},
    ]

# Layout dua kolom
col1, col2 = st.columns(2)

# ===============================
# 🧩 BAGIAN 1 - INPUT DATA
# ===============================
with col1:
    st.subheader("1️⃣ Input Data Hotel / Restoran")

    tipe_unit = st.selectbox("Pilih Tipe Unit", ["Hotel", "Restoran"])
    
    if tipe_unit == "Hotel":
        jumlah_kamar_str = st.text_input("Jumlah Kamar Hotel", value="50")
        tarif_kamar_str = st.text_input("Tarif per Kamar (Rp)", value="500000")
        okupansi = st.slider("Persentase Kamar Terisi (%)", 0, 100, 70)
        
        try:
            jumlah_kamar = int(jumlah_kamar_str.replace(".", "").replace(",", ""))
        except:
            jumlah_kamar = 50
        try:
            tarif_kamar = int(tarif_kamar_str.replace(".", "").replace(",", ""))
        except:
            tarif_kamar = 500000

    else:  # Restoran
        kapasitas = st.text_input("Kapasitas Restoran (jumlah pelanggan/hari)", value="100")
        rata_transaksi = st.text_input("Rata-rata Transaksi per Pelanggan (Rp)", value="100000")
        pengunjung = st.slider("Persentase Pengunjung Terlayani (%)", 0, 100, 80)
        
        try:
            kapasitas = int(kapasitas.replace(".", "").replace(",", ""))
        except:
            kapasitas = 100
        try:
            rata_transaksi = int(rata_transaksi.replace(".", "").replace(",", ""))
        except:
            rata_transaksi = 100000

    pajak = st.slider("Persentase Pajak (%)", 0, 100, 10)
    tanggal_awal = st.date_input("Tanggal Awal Proyeksi", value=datetime.today())

# ===============================
# 🧠 BAGIAN 2 - PROSES & VISUALISASI
# ===============================
with col2:
    st.subheader("2️⃣ Hasil Prediksi Pajak")

    if st.button("🚀 Proses Prediksi"):
        if tipe_unit == "Hotel":
            pendapatan_harian = jumlah_kamar * tarif_kamar * (okupansi / 100)
        else:
            pendapatan_harian = kapasitas * rata_transaksi * (pengunjung / 100)

        pajak_harian = pendapatan_harian * (pajak / 100)
        pajak_bulanan = pajak_harian * 30
        pajak_tahunan = pajak_harian * 365

        # Tampilkan hasil
        st.success(f"💰 **Pendapatan Harian:** Rp {pendapatan_harian:,.0f}")
        st.info(f"📆 **Pajak Bulanan (30 hari):** Rp {pajak_bulanan:,.0f}")
        st.info(f"📅 **Pajak Tahunan (365 hari):** Rp {pajak_tahunan:,.0f}")
        st.info(f"📈 **Pajak Harian:** Rp {pajak_harian:,.0f}")

        # Grafik
        data = pd.DataFrame({
            "Kategori": ["Pendapatan", "Pajak"],
            "Nilai (Rp)": [pendapatan_harian, pajak_harian]
        })

        fig, ax = plt.subplots(figsize=(5,3))
        ax.bar(data["Kategori"], data["Nilai (Rp)"], color=["green", "blue"])
        ax.set_title("Visualisasi Pendapatan vs Pajak Harian")
        ax.set_ylabel("Rp")
        st.pyplot(fig)

# ===============================
# 🗺️ BAGIAN 3 - PETA LOKASI DINAMIS
# ===============================
st.subheader("📍 Lokasi Hotel & Restoran di Cilegon")

with st.expander("➕ Tambah Lokasi Baru"):
    nama_lokasi = st.text_input("Nama Lokasi")
    lat_lokasi = st.number_input("Latitude", value=-6.0068, format="%.6f")
    lon_lokasi = st.number_input("Longitude", value=106.0491, format="%.6f")
    
    if st.button("Tambahkan Lokasi"):
        if nama_lokasi:
            st.session_state.locations.append({
                "nama": nama_lokasi,
                "lat": lat_lokasi,
                "lon": lon_lokasi
            })
            st.success(f"Lokasi '{nama_lokasi}' berhasil ditambahkan!")

# Tampilkan peta
m = folium.Map(location=[-6.006, 106.05], zoom_start=14)
for loc in st.session_state.locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=loc["nama"],
        icon=folium.Icon(color="red", icon="hotel" if "Hotel" in loc["nama"] else "cutlery", prefix="fa")
    ).add_to(m)

st_data = st_folium(m, width=700, height=400)

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("© 2025 Kelompok 4 – Sistem Informasi, Kampus Cilegon | Dibuat dengan ❤️ menggunakan Streamlit")

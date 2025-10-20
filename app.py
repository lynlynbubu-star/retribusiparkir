#%%writefile app.py
# ======================================================
# Aplikasi AI Dummy - Prediksi Potensi Retribusi Parkir
# Kota Cilegon
# Kelompok 4 - Sistem Informasi, Kampus Cilegon
# ======================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Judul Aplikasi
st.title("💡 AI Parkir Cilegon")
st.write("Simulasi Penerapan Kecerdasan Buatan dalam Menghitung Potensi Retribusi Parkir di Kota Cilegon")

# ==========================
# Bagian 1: Input Data
# ==========================
st.header("1️⃣ Input Data Kendaraan")

roda2 = st.number_input("Jumlah Kendaraan Roda Dua", min_value=0, value=41564)
roda4 = st.number_input("Jumlah Kendaraan Roda Empat", min_value=0, value=13369)
tarif = st.number_input("Tarif Retribusi per Kendaraan (Rp)", min_value=0, value=2000)
persentase_bayar = st.slider("Persentase Kendaraan yang Membayar (%)", 0, 100, 25)

# ==========================
# Bagian 2: Proses AI Dummy
# ==========================
st.header("2️⃣ Proses Prediksi AI")

# Fungsi perhitungan dummy AI
def hitung_retribusi(roda2, roda4, tarif, persentase):
    total = roda2 + roda4
    bayar = total * (persentase / 100)
    pendapatan_aktual = bayar * tarif
    potensi_ideal = total * tarif
    selisih = potensi_ideal - pendapatan_aktual
    return total, bayar, pendapatan_aktual, potensi_ideal, selisih

total, bayar, pendapatan_aktual, potensi_ideal, selisih = hitung_retribusi(roda2, roda4, tarif, persentase_bayar)

# Output hasil perhitungan
st.success(f"Total Kendaraan: {total:,}")
st.write(f"Potensi Ideal: Rp {potensi_ideal:,.0f}")
st.write(f"Pendapatan Aktual (AI Estimasi): Rp {pendapatan_aktual:,.0f}")
st.write(f"Kehilangan Potensi: Rp {selisih:,.0f}")

# ==========================
# Bagian 3: Visualisasi
# ==========================
st.header("3️⃣ Visualisasi Data")

data = pd.DataFrame({
    'Kategori': ['Potensi Ideal', 'Pendapatan Aktual', 'Kehilangan Potensi'],
    'Nilai (Rp)': [potensi_ideal, pendapatan_aktual, selisih]
})

fig, ax = plt.subplots()
ax.bar(data['Kategori'], data['Nilai (Rp)'])
ax.set_title("Grafik Perbandingan Potensi Retribusi Parkir")
ax.set_ylabel("Nilai (Rp)")
st.pyplot(fig)

# ==========================
# Bagian 4: Rekomendasi AI
# ==========================
st.header("4️⃣ Rekomendasi Sistem AI")

if persentase_bayar < 50:
    st.warning("⚠️ AI merekomendasikan peningkatan pengawasan pada area parkir liar.")
elif persentase_bayar < 80:
    st.info("ℹ️ Pendapatan cukup baik, namun masih ada potensi optimalisasi.")
else:
    st.success("✅ Sistem parkir berjalan efisien, potensi retribusi hampir maksimal!")

# ==========================
# Akhir Program
# ==========================
st.caption("© 2025 Kelompok 4 - Sistem Informasi Kampus Cilegon")

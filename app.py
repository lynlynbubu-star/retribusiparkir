#%%writefile app.py
# ======================================================
# Aplikasi AI Dummy - Prediksi Potensi Retribusi Parkir
# Kota Cilegon
# Kelompok 4 - Sistem Informasi, Kampus Cilegon
# ======================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul Aplikasi
st.set_page_config(page_title="AI Parkir Cilegon", layout="wide")
st.title("🚗 Aplikasi AI Parkir Cilegon")
st.markdown("### Prediksi dan Visualisasi Potensi Retribusi Parkir Menggunakan Kecerdasan Buatan")

# Layout: dua kolom
col1, col2 = st.columns(2)

# ===============================
# 🧩 BAGIAN 1 - INPUT DATA
# ===============================
with col1:
    st.subheader("1️⃣ Input Data Kendaraan")

    roda_dua = st.number_input("Jumlah Kendaraan Roda Dua", min_value=0, value=41564)
    roda_empat = st.number_input("Jumlah Kendaraan Roda Empat", min_value=0, value=13369)
    tarif_retribusi = st.number_input("Tarif Retribusi per Kendaraan (Rp)", min_value=0, value=2000)

    persentase_pembayar = st.slider("Persentase Kendaraan yang Bayar Retribusi (%)", 0, 100, 25)
    parkir_liar = st.slider("Perkiraan Parkir Liar (tidak dikelola Dishub) (%)", 0, 100, 30)

    st.info("Masukkan data sesuai kondisi lapangan Kota Cilegon")

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

        # Dummy AI (prediksi tren kenaikan retribusi)
        prediksi_naik = potensi_retribusi * 1.05  # misal AI prediksi naik 5%

        # ===============================
        # OUTPUT TEKS
        # ===============================
        st.success(f"💰 **Potensi Retribusi Parkir:** Rp {potensi_retribusi:,.0f}")
        st.warning(f"🚫 **Potensi Retribusi Hilang (Parkir Liar):** Rp {potensi_hilang:,.0f}")
        st.info(f"📈 **Prediksi AI (kenaikan 5%):** Rp {prediksi_naik:,.0f}")

        # ===============================
        # VISUALISASI DATA
        # ===============================
        data = pd.DataFrame({
            "Kategori": ["Bayar Retribusi", "Parkir Liar"],
            "Nilai (Rp)": [potensi_retribusi, potensi_hilang]
        })

        fig, ax = plt.subplots(figsize=(5, 3))
        ax.bar(data["Kategori"], data["Nilai (Rp)"])
        ax.set_title("Visualisasi Potensi Pendapatan vs Parkir Liar")
        ax.set_ylabel("Nilai (Rp)")
        st.pyplot(fig)

    else:
        st.info("Klik tombol **Proses Prediksi** untuk melihat hasil dan grafik.")

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("© 2025 Kelompok 4 – Sistem Informasi, Kampus Cilegon | Dibuat dengan ❤️ menggunakan Streamlit")



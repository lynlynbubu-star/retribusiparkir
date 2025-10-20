%%writefile app.py
# ======================================================
# Aplikasi AI Dummy - Prediksi Potensi Retribusi Parkir
# Kota Cilegon
# Kelompok 4 - Sistem Informasi, Kampus Cilegon
# ======================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="AI Parkir Cilegon", layout="wide")
st.title("🚗 Aplikasi AI Parkir Cilegon")
st.markdown("### Prediksi dan Visualisasi Potensi Retribusi Parkir Menggunakan Kecerdasan Buatan")

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
        prediksi_naik = potensi_retribusi * 1.05  # simulasi kenaikan 5%

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
        ax.bar(data["Kategori"], data["Nilai (Rp)"], color=["green", "red"])
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





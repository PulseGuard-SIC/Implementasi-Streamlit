import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

data = pd.DataFrame({
    'Timestamp': pd.date_range('2024-07-08', periods=100, freq='H'),
    'Body Temperature (C)': np.random.uniform(36.0, 37.5, 100),
    'Heart Rate (bpm)': np.random.randint(60, 100, 100)
})

st.set_page_config(page_title='PulseGuard', layout='wide', initial_sidebar_state='expanded')
st.title('PulseGuard: Deteksi Penyakit Jantung')

logo_image = Image.open('Logo.png')
st.sidebar.image(logo_image, caption='Logo PulseGuard', width=150)

st.write('Aplikasi untuk memantau data sensor tubuh dan detak jantung.')

st.sidebar.subheader('Menu Utama')
menu_selection = st.sidebar.radio('Pilih Halaman:', ('Beranda', 'Tentang', 'Kontak'))

if menu_selection == 'Tentang':
    st.subheader('Tentang PulseGuard')
    st.markdown("""
    Aplikasi *PulseGuard* dirancang untuk memantau parameter-parameter seperti suhu tubuh dan detak jantung,
    yang dapat memberikan indikasi awal kondisi kesehatan jantung.
    
    *Fitur:*
    - Visualisasi suhu tubuh dan detak jantung.
    - Analisis sederhana korelasi antara suhu tubuh dan detak jantung.
    - Informasi tentang penyakit jantung global.
    """)
elif menu_selection == 'Kontak':
    st.subheader('Kontak Kami')
    st.markdown("""
    *Email:*
    info@pulseguard.com
    
    *Telepon:*
    +62 123 4567
    """)

st.subheader('Penyakit Jantung Global')
st.markdown("""
Penyakit jantung merupakan salah satu masalah kesehatan utama di seluruh dunia yang mempengaruhi jutaan orang setiap tahunnya. Berikut ini adalah beberapa poin penting tentang penyakit jantung secara global:

1. Pandemi Penyakit Jantung: Penyakit jantung termasuk penyebab utama kematian di seluruh dunia. Menurut World Health Organization (WHO), penyakit jantung dan stroke bersama-sama menyebabkan sekitar 17,9 juta kematian setiap tahunnya.

2. Faktor Risiko Utama: Beberapa faktor risiko utama penyakit jantung meliputi merokok, tekanan darah tinggi, kolesterol tinggi, diabetes, serta gaya hidup tidak sehat seperti kurangnya aktivitas fisik dan pola makan yang tidak sehat.

3. Penyebab: Penyakit jantung dapat disebabkan oleh berbagai kondisi, termasuk penyempitan atau sumbatan pembuluh darah yang memasok darah ke jantung (penyakit arteri koroner), gangguan pada katup jantung, serta kelainan jantung lainnya.
""")

st.sidebar.subheader('Pengaturan')
plot_type = st.sidebar.radio('Pilih Jenis Plot:', ('Line Plot', 'Histogram'))

st.subheader('Visualisasi Data')

if plot_type == 'Line Plot':
    st.subheader('Body Temperature')
    fig_temp, ax_temp = plt.subplots(figsize=(10, 5))
    ax_temp.plot(data['Timestamp'], data['Body Temperature (C)'], marker='o', color='#3498DB')
    ax_temp.set_xlabel('Timestamp')
    ax_temp.set_ylabel('Body Temperature (C)')
    st.pyplot(fig_temp)

    st.subheader('Heart Rate')
    fig_hr, ax_hr = plt.subplots(figsize=(10, 5))
    ax_hr.plot(data['Timestamp'], data['Heart Rate (bpm)'], marker='o', color='#E74C3C')
    ax_hr.set_xlabel('Timestamp')
    ax_hr.set_ylabel('Heart Rate (bpm)')
    st.pyplot(fig_hr)

elif plot_type == 'Histogram':
    st.subheader('Distribusi Body Temperature')
    fig_dist_temp, ax_dist_temp = plt.subplots(figsize=(8, 4))
    sns.histplot(data['Body Temperature (C)'], bins=20, kde=True, color='#3498DB', ax=ax_dist_temp)
    ax_dist_temp.set_xlabel('Body Temperature (C)')
    ax_dist_temp.set_ylabel('Frequency')
    st.pyplot(fig_dist_temp)

    st.subheader('Distribusi Heart Rate')
    fig_dist_hr, ax_dist_hr = plt.subplots(figsize=(8, 4))
    sns.histplot(data['Heart Rate (bpm)'], bins=20, kde=True, color='#E74C3C', ax=ax_dist_hr)
    ax_dist_hr.set_xlabel('Heart Rate (bpm)')
    ax_dist_hr.set_ylabel('Frequency')
    st.pyplot(fig_dist_hr)

age_range = st.sidebar.slider('Pilih rentang usia:', 0, 100, (20, 80))

st.subheader('Analisis Sederhana')

correlation = data['Body Temperature (C)'].corr(data['Heart Rate (bpm)'])
st.write(f'Korelasi antara Body Temperature dan Heart Rate: {correlation:.2f}')



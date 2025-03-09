import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
st.write("Working directory:", os.getcwd())
st.write("Files in current directory:", os.listdir())


st.title("Dashboard Bike Sharing - Full Analysis")

@st.cache
def load_data_day():
    df_day = pd.read_csv('../data/day.csv')
    df_day['dteday'] = pd.to_datetime(df_day['dteday'])
    df_day['day_of_week'] = df_day['dteday'].dt.day_name()
    return df_day

@st.cache
def load_data_hour():
    df_hour = pd.read_csv('../data/hour.csv')
    df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])
    df_hour['hr'] = df_hour['hr'].astype(int)

    def time_of_day(hr):
        if 5 <= hr < 12:
            return 'Pagi'
        elif 12 <= hr < 17:
            return 'Siang'
        elif 17 <= hr < 21:
            return 'Sore'
        else:
            return 'Malam'
    df_hour['time_category'] = df_hour['hr'].apply(time_of_day)
    return df_hour

df_day = load_data_day()
df_hour = load_data_hour()

tab1, tab2, tab3 = st.tabs(["Pengaruh Cuaca (Harian)", "Pola Penggunaan Per Jam", "Data Mentah"])

# -----------------------------------------------------------------------------
# TAB 1: Pengaruh Cuaca (Harian)
# -----------------------------------------------------------------------------
with tab1:
    st.subheader("Pengaruh Cuaca Terhadap Penyewaan (Harian)")

    # Scatter plot: temp vs cnt
    fig1, ax1 = plt.subplots()
    ax1.scatter(df_day['temp'], df_day['cnt'], alpha=0.6, color='darkgreen')
    ax1.set_title('Pengaruh Temperatur vs. Penyewaan (Harian)')
    ax1.set_xlabel('Temperatur (Normalized)')
    ax1.set_ylabel('Jumlah Penyewaan')
    st.pyplot(fig1)

    # Heatmap korelasi (kolom numerik)
    fig2, ax2 = plt.subplots(figsize=(8,6))
    corr_day = df_day.select_dtypes(include='number').corr()
    sns.heatmap(corr_day, annot=True, cmap='coolwarm', ax=ax2)
    ax2.set_title('Heatmap Korelasi (Data Harian)')
    st.pyplot(fig2)

    st.markdown("""
    **Insight Singkat**:
    - Terdapat korelasi positif antara temperatur (`temp`) dan jumlah penyewaan (`cnt`).
    - Kolom `hum` (kelembaban) dan `windspeed` cenderung berkorelasi negatif dengan penyewaan.
    """)

# -----------------------------------------------------------------------------
# TAB 2: Pola Penggunaan Per Jam
# -----------------------------------------------------------------------------
with tab2:
    st.subheader("Pola Penggunaan Per Jam")

    selected_hr = st.slider("Pilih Jam (0-23)", 0, 23, 12)
    filtered_data = df_hour[df_hour['hr'] == selected_hr]
    data_by_date = filtered_data.groupby('dteday')['cnt'].sum().reset_index()

    # Line chart agar lebih mudah dibaca
    fig3, ax3 = plt.subplots(figsize=(10,5))
    ax3.plot(data_by_date['dteday'], data_by_date['cnt'], color='skyblue', marker='o')
    ax3.set_title(f'Penyewaan Sepeda pada Jam {selected_hr} per Tanggal')
    ax3.set_xlabel('Tanggal')
    ax3.set_ylabel('Jumlah Penyewaan')
    plt.xticks(rotation=45)

    # Jika data terlalu banyak, skip sebagian label
    if len(data_by_date) > 30:
        step = len(data_by_date) // 10
        for index, label in enumerate(ax3.xaxis.get_ticklabels()):
            if index % step != 0:
                label.set_visible(False)

    st.pyplot(fig3)

    # Tampilkan rata-rata penyewaan pada jam yang dipilih
    avg_selected_hr = data_by_date['cnt'].mean()
    st.markdown(f"**Rata-rata Penyewaan pada Jam {selected_hr}:** {avg_selected_hr:.2f}")

    st.markdown("""
    Grafik di atas menampilkan jumlah penyewaan sepeda (diakumulasikan per tanggal) 
    untuk jam tertentu yang dipilih pada slider. Dengan ini, Anda dapat melihat bagaimana 
    penggunaan sepeda berfluktuasi dari hari ke hari pada jam tersebut.
    """)

    st.subheader("Rata-rata Penyewaan Per Jam (Keseluruhan)")
    avg_hourly = df_hour.groupby('hr')['cnt'].mean().reset_index()
    fig4, ax4 = plt.subplots(figsize=(10,5))
    ax4.bar(avg_hourly['hr'], avg_hourly['cnt'], color='coral')
    ax4.set_title('Rata-rata Penyewaan Sepeda Per Jam')
    ax4.set_xlabel('Jam')
    ax4.set_ylabel('Rata-rata Penyewaan')
    st.pyplot(fig4)

    st.subheader("Rata-rata Penyewaan Berdasarkan Kategori Waktu")
    avg_time_cat = df_hour.groupby('time_category')['cnt'].mean().reset_index()
    fig5, ax5 = plt.subplots(figsize=(6,4))
    ax5.bar(avg_time_cat['time_category'], avg_time_cat['cnt'], color='green')
    ax5.set_title('Rata-rata Penyewaan Berdasarkan Kategori Waktu')
    ax5.set_xlabel('Kategori Waktu')
    ax5.set_ylabel('Rata-rata Penyewaan')
    st.pyplot(fig5)

    st.markdown("""
    **Insight Singkat**:
    - Penggunaan sepeda tertinggi biasanya terjadi pada jam 17-18 (Sore) dan jam 7-8 (Pagi).
    - Kategori waktu "Sore" menunjukkan rata-rata penyewaan tertinggi dibanding "Pagi", "Siang", dan "Malam".
    """)

# -----------------------------------------------------------------------------
# TAB 3: Data Mentah
# -----------------------------------------------------------------------------
with tab3:
    st.subheader("Data Mentah")
    st.write("**Dataset Harian (5 Baris Pertama):**")
    st.dataframe(df_day.head())

    st.write("**Dataset Per Jam (5 Baris Pertama):**")
    st.dataframe(df_hour.head())

    if st.checkbox("Tampilkan Seluruh Data (Harian)"):
        st.dataframe(df_day)

    if st.checkbox("Tampilkan Seluruh Data (Per Jam)"):
        st.dataframe(df_hour)

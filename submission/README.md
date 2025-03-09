# Proyek Analisis Data Bike Sharing

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penggunaan Bike Sharing berdasarkan dua set data:
1. **Data Harian (`day.csv`)**: Menyimpan informasi agregat penyewaan sepeda per hari.
2. **Data Per Jam (`hour.csv`)**: Menyimpan informasi penyewaan sepeda secara detail per jam.

Melalui proyek ini, kita berusaha menjawab beberapa pertanyaan bisnis, di antaranya:
- Bagaimana pengaruh variabel cuaca (seperti temperatur, kelembaban, dan kecepatan angin) terhadap jumlah penyewaan sepeda harian?
- Bagaimana pola penggunaan sepeda per jam, dan jam berapa saja yang menjadi peak usage?
- Adakah perbedaan penggunaan sepeda di akhir pekan vs. hari kerja, atau pada musim tertentu?

Hasil analisis kemudian disajikan dalam bentuk **dashboard interaktif** menggunakan Streamlit.

---

## Struktur Folder
submission 
├── dashboard 
│ |── dashboard.py 
├── data 
│ ├── day.csv 
│ └── hour.csv
├── notebook.ipynb
├── README.md 
├── requirements.txt
└── url.txt

---

## Cara Instalasi

1. **Pastikan Python 3 dan pip telah terinstal** di komputer kamu.  
   - Kamu bisa mengecek versi Python dengan `python --version` atau `python3 --version`.
   - Cek pip dengan `pip --version`.

2. **Install Library yang Dibutuhkan**  
   Di dalam folder `submission`, jalankan perintah:
   ```bash
   pip install -r requirements.txt

Menjalankan Notebook
Buka notebook.ipynb menggunakan Jupyter Notebook atau Google Colab untuk melihat proses analisis data mulai dari Gathering Data, Data Wrangling, EDA, hingga Analisis Lanjutan.
Jalankan setiap cell agar kamu bisa melihat output dan visualisasi yang dihasilkan.

Menjalankan Dashboard
Pastikan kamu berada di folder submission yang berisi file dashboard.py di dalam folder dashboard serta folder data.
Jalankan perintah berikut di terminal/command prompt:
streamlit run dashboard/dashboard.py
Jika Windows tidak mengenali perintah streamlit, gunakan:
python -m streamlit run dashboard/dashboard.py

Buka browser dan akses URL

Navigasi Dashboard:
Tab "Pengaruh Cuaca (Harian)": Menampilkan scatter plot temperatur vs. penyewaan harian serta heatmap korelasi.
Tab "Pola Penggunaan Per Jam": Menampilkan slider untuk memilih jam dan melihat grafik penyewaan per tanggal, juga grafik rata-rata penyewaan per jam dan per kategori waktu.
Tab "Data Mentah": Memperlihatkan beberapa baris awal dari dataset harian dan per jam, serta opsi untuk menampilkan seluruh data.

File Pendukung
requirements.txt: Daftar library yang dibutuhkan agar analisis data dan dashboard dapat berjalan.
url.txt: Berisi URL dashboard


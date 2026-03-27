# 🌤️ Aplikasi Cuaca

Aplikasi web berbasis **Streamlit** untuk mengecek cuaca terkini di kota manapun di seluruh dunia, lengkap dengan rekomendasi aktivitas berdasarkan kondisi cuaca.

## ✨ Fitur

- 🔍 Pencarian cuaca real-time berdasarkan nama kota
- 🌡️ Informasi suhu, kelembaban, tekanan udara, dan kecepatan angin
- 🌅 Informasi waktu matahari terbit dan terbenam
- 👕 Rekomendasi pakaian berdasarkan cuaca
- 🏃 Rekomendasi aktivitas outdoor & indoor
- 💡 Tips & saran berdasarkan kondisi cuaca
- 🇮🇩 Antarmuka dalam Bahasa Indonesia

## 🖼️ Preview

> Masukkan nama kota → Lihat cuaca terkini → Dapatkan rekomendasi aktivitas

## 🛠️ Teknologi

| Teknologi | Keterangan |
|-----------|------------|
| [Python 3.9+](https://www.python.org/) | Bahasa pemrograman utama |
| [Streamlit](https://streamlit.io/) | Framework web app |
| [OpenWeatherMap API](https://openweathermap.org/api) | Sumber data cuaca |
| [Requests](https://requests.readthedocs.io/) | HTTP client library |

## 📋 Prasyarat

- Python 3.9 atau lebih baru
- API Key dari [OpenWeatherMap](https://openweathermap.org/api) (gratis)

## 🚀 Instalasi & Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/username/aplikasi-cuaca.git
cd aplikasi-cuaca
```

### 2. Buat Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Environment Variable

Salin file `.env.example` menjadi `.env` dan isi dengan API key Anda:

```bash
cp .env.example .env
```

Buka `.env` dan isi:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

> 💡 Dapatkan API key gratis di: https://home.openweathermap.org/api_keys

### 5. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser pada `http://localhost:8501`

## 📁 Struktur Proyek

```
aplikasi-cuaca/
├── app.py                  # File utama aplikasi Streamlit
├── requirements.txt        # Daftar dependensi Python
├── .env                    # Environment variables (tidak di-commit)
├── .env.example            # Template environment variables
├── .gitignore              # File yang diabaikan Git
└── README.md               # Dokumentasi proyek ini
```

## 🌐 Deploy ke Streamlit Cloud

1. Push repository ke GitHub
2. Buka [share.streamlit.io](https://share.streamlit.io/)
3. Hubungkan repository GitHub Anda
4. Tambahkan `OPENWEATHER_API_KEY` di **Settings → Secrets**:
   ```toml
   OPENWEATHER_API_KEY = "your_api_key_here"
   ```
5. Klik **Deploy**

## 📝 Penggunaan

1. Ketikkan nama kota di kolom pencarian (contoh: `Jakarta`, `Samarinda`, `Surabaya`)
2. Klik tombol **🔍 Cari**
3. Lihat informasi cuaca yang ditampilkan
4. Klik **🔽 Tampilkan Rekomendasi Aktivitas** untuk mendapatkan saran aktivitas

## 🤝 Kontribusi

Kontribusi sangat disambut! Silakan:

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b fitur/nama-fitur`)
3. Commit perubahan Anda (`git commit -m 'Menambahkan fitur X'`)
4. Push ke branch (`git push origin fitur/nama-fitur`)
5. Buat Pull Request

## 📄 Lisensi

Proyek ini dibuat untuk keperluan **Tugas UAS Pemrograman Dasar**.

## 👤 Biodata Pengembang

<div align="center">

### Dhede Febrian Purnawiranto

🎓 D3 Teknik Informatika — Jurusan Teknologi Informasi  
🏫 Politeknik Negeri Samarinda  
📅 Angkatan 2025 

---

📚 **Tentang Proyek Ini**  
Aplikasi Cuaca ini dibuat sebagai **Tugas UAS Mata Kuliah Pemrograman Dasar** Semester 1.  
Dibangun menggunakan Python & Streamlit dengan integrasi OpenWeatherMap API.

🛠️ **Teknologi yang Digunakan**  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-orange?style=for-the-badge)

</div>

---

> Data cuaca disediakan oleh [OpenWeatherMap](https://openweathermap.org/) API.

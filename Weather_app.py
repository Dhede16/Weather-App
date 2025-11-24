import streamlit as st
import requests
from datetime import datetime

API_KEY = "69fa9212e5e1baf54a269c65464abb90"

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Cuaca",
    page_icon="🌤️",
    layout="centered"
)

# CSS untuk styling
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1E88E5;
        font-size: 3em;
        margin-bottom: 0;
    }
    .weather-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 20px 0;
    }
    .temp {
        font-size: 4em;
        font-weight: bold;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Judul aplikasi
st.markdown('<h1 class="main-title">🌤️ Aplikasi Cuaca</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666;">Cek cuaca terkini di kota manapun!</p>', unsafe_allow_html=True)

# Input kota
col1, col2 = st.columns([3, 1])
with col1:
    city = st.text_input("🌍 Masukkan nama kota:", placeholder="Contoh: Jakarta, Samarinda, Bali")

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    search_btn = st.button("🔍 Cari", use_container_width=True)

# Fungsi untuk mendapatkan data cuaca
def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "id"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None

# Proses pencarian cuaca
if search_btn or city:
    if not city:
        st.warning("⚠️ Silakan masukkan nama kota!")
    else:
        with st.spinner("🔄 Mengambil data cuaca..."):
            weather_data = get_weather(city)
            
            if weather_data and weather_data.get("cod") != "404":
                # Ekstrak data
                temp = weather_data["main"]["temp"]
                feels_like = weather_data["main"]["feels_like"]
                humidity = weather_data["main"]["humidity"]
                pressure = weather_data["main"]["pressure"]
                wind_speed = weather_data["wind"]["speed"]
                description = weather_data["weather"][0]["description"]
                icon = weather_data["weather"][0]["icon"]
                city_name = weather_data["name"]
                country = weather_data["sys"]["country"]
                
                # Tampilkan data cuaca
                st.markdown(f"""
                    <div class="weather-card">
                        <h2>📍 {city_name}, {country}</h2>
                        <img src="http://openweathermap.org/img/wn/{icon}@4x.png" width="150">
                        <div class="temp">{temp:.1f}°C</div>
                        <h3>{description.capitalize()}</h3>
                    </div>
                """, unsafe_allow_html=True)
                
                # Detail cuaca dalam kolom
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("🌡️ Terasa Seperti", f"{feels_like:.1f}°C")
                    st.metric("💨 Kecepatan Angin", f"{wind_speed} m/s")
                
                with col2:
                    st.metric("💧 Kelembaban", f"{humidity}%")
                    st.metric("🔽 Tekanan", f"{pressure} hPa")
                
                with col3:
                    temp_min = weather_data["main"]["temp_min"]
                    temp_max = weather_data["main"]["temp_max"]
                    st.metric("🌡️ Suhu Min", f"{temp_min:.1f}°C")
                    st.metric("🌡️ Suhu Max", f"{temp_max:.1f}°C")
                
                # Informasi tambahan
                sunrise = datetime.fromtimestamp(weather_data["sys"]["sunrise"]).strftime("%H:%M")
                sunset = datetime.fromtimestamp(weather_data["sys"]["sunset"]).strftime("%H:%M")
                
                st.markdown("---")
                col1, col2 = st.columns(2)
                with col1:
                    st.info(f"🌅 Matahari Terbit: {sunrise}")
                with col2:
                    st.info(f"🌇 Matahari Terbenam: {sunset}")
                
            elif weather_data and weather_data.get("cod") == "404":
                st.error("❌ Kota tidak ditemukan! Periksa kembali nama kota Anda.")
            else:
                st.error("❌ Kota tidak ditemukan! Periksa kembali nama kota Anda.")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
        <p>Aplikasi Cuaca Tugas UAS Pemograman Dasar </p>
    </div>
""", unsafe_allow_html=True)
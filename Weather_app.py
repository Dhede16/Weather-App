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
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .temp {
        font-size: 4em;
        font-weight: bold;
        margin: 20px 0;
    }
    .activity-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin: 10px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .recommendation-item {
        background: rgba(255,255,255,0.2);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        backdrop-filter: blur(10px);
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
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()


# Fungsi untuk memberikan rekomendasi aktivitas
def get_activity_recommendations(weather_data):
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    weather_main = weather_data["weather"][0]["main"].lower()
    
    recommendations = {
        "outdoor": [],
        "indoor": [],
        "tips": [],
        "clothing": []
    }
    
    # Rekomendasi berdasarkan cuaca utama
    if "rain" in weather_main or "drizzle" in weather_main:
        recommendations["indoor"] = [
            "☕ Nikmati kopi hangat di kafe",
            "📚 Waktu yang tepat untuk membaca buku",
            "🎬 Menonton film di rumah",
            "🎨 Melakukan hobi indoor seperti menggambar atau memasak"
        ]
        recommendations["tips"] = [
            "☂️ Jangan lupa bawa payung!",
            "🚗 Hati-hati berkendara, jalan mungkin licin",
            "👟 Gunakan alas kaki yang tidak licin"
        ]
        recommendations["clothing"] = [
            "🧥 Jaket tahan air",
            "👢 Sepatu tertutup/boots",
            "☂️ Payung atau jas hujan"
        ]
    
    elif "thunderstorm" in weather_main:
        recommendations["indoor"] = [
            "🏠 Tetap di dalam ruangan yang aman",
            "📱 Cabut perangkat elektronik dari stop kontak",
            "🎮 Main game atau aktivitas indoor lainnya",
            "👨‍👩‍👧‍👦 Quality time bersama keluarga"
        ]
        recommendations["tips"] = [
            "⚠️ Hindari aktivitas outdoor",
            "🚫 Jangan berteduh di bawah pohon",
            "📵 Hindari menggunakan telepon dengan kabel"
        ]
        recommendations["clothing"] = [
            "🏠 Tetap di dalam ruangan",
            "🧥 Jaket tebal jika harus keluar"
        ]
    
    elif "cloud" in weather_main:
        if temp < 25:
            recommendations["outdoor"] = [
                "🚶 Jalan-jalan santai di taman",
                "🚴 Bersepeda keliling kota",
                "📸 Fotografi landscape",
                "🏃 Jogging atau olahraga ringan"
            ]
        else:
            recommendations["outdoor"] = [
                "🏊 Berenang",
                "⛱️ Piknik di taman",
                "🎣 Memancing",
                "🏐 Olahraga outdoor"
            ]
        recommendations["tips"] = [
            "😎 Cuaca cukup nyaman untuk beraktivitas",
            "💧 Tetap bawa air minum",
            "🧴 Gunakan sunscreen jika keluar lama"
        ]
    
    elif "clear" in weather_main:
        if temp > 30:
            recommendations["outdoor"] = [
                "🏊 Berenang di kolam renang",
                "🏖️ Pergi ke pantai",
                "🍦 Makan es krim",
                "🌳 Cari tempat teduh untuk piknik"
            ]
            recommendations["tips"] = [
                "🥵 Cuaca sangat panas, hindari aktivitas berat",
                "💧 Minum air yang banyak",
                "🧢 Gunakan topi dan kacamata hitam",
                "🧴 Wajib pakai sunscreen SPF tinggi"
            ]
            recommendations["clothing"] = [
                "👕 Pakaian tipis dan menyerap keringat",
                "🧢 Topi atau payung",
                "😎 Kacamata hitam",
                "👟 Sandal atau sepatu yang nyaman"
            ]
        else:
            recommendations["outdoor"] = [
                "🚴 Bersepeda",
                "🏃 Jogging atau lari pagi/sore",
                "⛰️ Hiking atau mendaki",
                "📸 Fotografi outdoor",
                "⚽ Olahraga lapangan"
            ]
            recommendations["tips"] = [
                "😊 Cuaca cerah sempurna untuk beraktivitas!",
                "💧 Tetap hidrasi dengan baik",
                "🧴 Pakai sunscreen"
            ]
            recommendations["clothing"] = [
                "👕 Pakaian casual dan nyaman",
                "😎 Kacamata hitam",
                "🧢 Topi jika perlu"
            ]
    
    # Rekomendasi berdasarkan suhu
    if temp < 20:
        recommendations["clothing"].extend([
            "🧥 Jaket atau sweater",
            "👖 Celana panjang"
        ])
        recommendations["tips"].append("🥶 Cuaca dingin, kenakan pakaian hangat")
    
    # Rekomendasi berdasarkan kelembaban
    if humidity > 80:
        recommendations["tips"].append("💦 Kelembaban tinggi, mungkin terasa gerah")
    
    # Rekomendasi berdasarkan kecepatan angin
    if wind_speed > 10:
        recommendations["tips"].append("💨 Angin kencang, hati-hati dengan benda yang mudah terbang")
    
    # Jika tidak ada rekomendasi outdoor, tambahkan indoor default
    if not recommendations["outdoor"]:
        recommendations["indoor"] = [
            "🏠 Tetap di dalam ruangan",
            "📺 Menonton TV atau streaming",
            "🎮 Bermain game",
            "📖 Membaca buku",
            "🍳 Memasak makanan favorit"
        ]
    
    # Jika tidak ada tips, tambahkan default
    if not recommendations["tips"]:
        recommendations["tips"] = ["😊 Cuaca cukup nyaman untuk beraktivitas"]
    
    # Jika tidak ada clothing, tambahkan default
    if not recommendations["clothing"]:
        recommendations["clothing"] = ["👕 Pakaian casual sesuai kenyamanan"]
    
    return recommendations

# Simpan weather_data di session state
if 'weather_data' not in st.session_state:
    st.session_state.weather_data = None
if 'show_recommendations' not in st.session_state:
    st.session_state.show_recommendations = False

# Proses pencarian cuaca
if search_btn or city:
    if not city:
        st.warning("⚠️ Silakan masukkan nama kota!")
    else:
        with st.spinner("🔄 Mengambil data cuaca..."):
            weather_data = get_weather(city)
            
            if weather_data and weather_data.get("cod") != "404":
                # Simpan ke session state
                st.session_state.weather_data = weather_data
                
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
                st.session_state.weather_data = None
            else:
                st.error("❌ Terjadi kesalahan saat mengambil data cuaca!")
                st.session_state.weather_data = None

# Tombol rekomendasi aktivitas
if st.session_state.weather_data:
    
    if st.button("🔽 Tampilkan Rekomendasi Aktivitas", use_container_width=True):
        st.session_state.show_recommendations = True
    
    if st.session_state.show_recommendations:
        st.markdown("---")
        st.markdown('<h3 style="text-align: center;">Rekomendasi Aktivitas Berdasarkan Cuaca</h3>', unsafe_allow_html=True)
        
        recommendations = get_activity_recommendations(st.session_state.weather_data)
        
        # Tampilkan rekomendasi
        col1, col2 = st.columns(2)
        
        with col1:
            if recommendations["outdoor"]:
                st.markdown('<h3 style="text-align: center;">🌳 Aktivitas Outdoor</h3>', unsafe_allow_html=True)
                for activity in recommendations["outdoor"]:
                    st.success(activity)
            
            if recommendations["indoor"]:
                st.markdown('<h3 style="text-align: center;">🏠 Aktivitas Indoor</h3>', unsafe_allow_html=True)
                for activity in recommendations["indoor"]:
                    st.info(activity)
        
        with col2:
            st.markdown('<h3 style="text-align: center;">👕 Rekomendasi Pakaian</h3>', unsafe_allow_html=True)
            for clothing in recommendations["clothing"]:
                st.warning(clothing)

        col1, col2, col3 = st.columns([1,4,1])

        with col2:
            st.markdown('<h3 style="text-align: center;">💡 Tips & Saran</h3>', unsafe_allow_html=True)
            for tip in recommendations["tips"]:
                st.success(tip)

    if st.session_state.show_recommendations:
        if st.button("🔼 Tutup Rekomendasi", use_container_width=True):
            st.session_state.show_recommendations = False
            st.rerun()
            
# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 20px;">
        <p>Aplikasi Cuaca Tugas UAS Pemrograman Dasar</p>
    </div>
""", unsafe_allow_html=True)

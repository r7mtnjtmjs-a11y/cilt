import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="Bella Skin AI", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #F5F5DC;
    }
    .stButton>button {
        background-color: #B2AC88;
        color: white;
        border-radius: 25px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #8F8A6B;
        border: none;
    }
    .profile-box {
        padding: 20px;
        background-color: white;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #E6E6E6;
        color: #555;
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

genai.configure(api_key="AIzaSyDEVQ2G_Rqq60ZjBk6APfoEdvc7fCL8-yA")
model = genai.GenerativeModel('gemini-1.5-flash')

if 'user_data' not in st.session_state:
    st.session_state.user_data = {"name": "", "age": 0, "skin_type": "", "registered": False}

if not st.session_state.user_data["registered"]:
    st.title("🌿 Bella Skin")
    st.write("Kişisel cilt asistanın için profilini oluştur.")
    
    name = st.text_input("İsminiz nedir?")
    age = st.number_input("Yaşınız?", min_value=0, max_value=100, step=1)
    skin_type = st.selectbox("Cilt tipini biliyor musun?", 
                            ["Seçiniz", "Yağlı", "Kuru", "Karma", "Hassas", "Bilmiyorum, analiz edelim"])
    
    if st.button("Kaydol ve Başla"):
        if name and age > 0:
            st.session_state.user_data = {
                "name": name,
                "age": age,
                "skin_type": skin_type,
                "registered": True
            }
            st.rerun()
        else:
            st.warning("Lütfen ismini ve yaşını boş bırakma.")

else:
    st.title(f"Selam, {st.session_state.user_data['name']} ✨")
    
    st.markdown(f"""
    <div class="profile-box">
        <b>Profil Bilgilerin:</b><br>
         Yaş: {st.session_state.user_data['age']} | Cilt: {st.session_state.user_data['skin_type']}
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📸 Yüz Analizi", "🔍 Ürün Tara"])

    with tab1:
        st.write("Cilt durumunu anlamam için bir selfie çek.")
        face_img = st.camera_input("Selfie çek", key="face_camera")
        if face_img:
            st.info("Analiz sistemi hazırlanıyor...")

    with tab2:
        st.write("Ürünün arkasındaki içerik listesini çek.")
        prod_img = st.camera_input("Ürünü tara", key="prod_camera")
        if prod_img:
            st.info(f"{st.session_state.user_data['name']}, bu ürünü senin için inceliyorum...")

    if st.button("Profili Sıfırla"):
        st.session_state.user_data["registered"] = False
        st.rerun()

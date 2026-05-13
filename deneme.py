import streamlit as st
import google.generativeai as genai
from PIL import Image
import pytesseract

st.set_page_config(page_title="Bella Skin AI", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #F9F7F2 !important;
    }
    
    h1 {
        color: #5D6D7E !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 300 !important;
        text-align: center;
        margin-bottom: 0px;
    }

    .stCameraInput > div {
        border-radius: 35px !important;
        overflow: hidden !important;
        border: 8px solid white !important;
        box-shadow: 0 15px 35px rgba(0,0,0,0.05) !important;
    }

    button {
        border-radius: 50px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stInfo {
        background-color: white !important;
        border: none !important;
        border-radius: 30px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.04) !important;
        padding: 30px !important;
        color: #5D6D7E !important;
    }

    .stMarkdown p {
        color: #7F8C8D;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 Cilt Asistanım")
st.write("Stitch tasarımıyla içerik analizi")

GOOGLE_API_KEY = "AIzaSyDEVQ2G_Rgq6OZjBk6APfoEdvC7fCL8-yA" 
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

uploaded_file = st.camera_input("")

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, use_container_width=True)
    
    with st.spinner('Gemini inceliyor... ✨'):
        try:
            text = pytesseract.image_to_string(img)
            prompt = f"Bir cilt bakımı uzmanı gibi davran. Şu içerik listesini analiz et: {text}. Eğer sivilce yapan veya tahriş edici maddeler varsa nazik ve soft bir dille uyar. Türkçe cevap ver."
            response = model.generate_content(prompt)
            st.markdown("---")
            st.info(response.text)
        except Exception as e:
            st.error("Bir bağlantı sorunu oluştu.")

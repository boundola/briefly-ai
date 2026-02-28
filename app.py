import streamlit as st
import google.generativeai as genai

# টাইটেল এবং স্টাইল
st.set_page_config(page_title="ProBrief AI 🚀", layout="centered")

# Secrets থেকে API Key নেওয়া
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    st.error("API Key not found in Secrets!")
    st.stop()

# ডিজাইন
st.markdown("""
    <style>
    .stButton>button { background-color: #28a745; color: white; border-radius: 8px; width: 100%; height: 50px; font-size: 18px; }
    .donate-btn { background-color: #ffdd00; color: black; padding: 12px; text-decoration: none; border-radius: 8px; font-weight: bold; display: block; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# সাইডবার
with st.sidebar:
    st.title("💰 Monetization")
    st.markdown('<a href="https://www.buymeacoffee.com/YOUR_USER" target="_blank" class="donate-btn">☕ Support me: Buy Me a Coffee</a>', unsafe_allow_html=True)
    st.write("---")
    st.info("📢 Ad Space: Google AdSense")

st.title("ProBrief AI 🚀")
st.write("আপনার ক্লায়েন্ট মিটিংয়ের অডিও ফাইল আপলোড করুন এবং এক ক্লিকেই সামারি পান।")

uploaded_file = st.file_uploader("অডিও ফাইল সিলেক্ট করুন (MP3/WAV)", type=["mp3", "wav"])

if st.button("Generate Magic Summary ✨"):
    if uploaded_file:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            with st.spinner('প্রসেস হচ্ছে...'):
                audio_data = uploaded_file.read()
                prompt = "Provide a professional summary and a list of action items for a freelancer from this audio."
                response = model.generate_content([prompt, {"mime_type": "audio/mp3", "data": audio_data}])
                st.markdown("### ✅ Result")
                st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("দয়া করে ফাইল আপলোড করুন।")

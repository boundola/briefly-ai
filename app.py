import streamlit as st
import google.generativeai as genai

# অ্যাপের টাইটেল এবং স্টাইল
st.set_page_config(page_title="BrieflyAI - Professional Meeting Summarizer", layout="centered")

# ডিজাইন কাস্টমাইজেশন (আমেরিকান ফ্রিল্যান্সারদের জন্য ক্লিন ডিজাইন)
st.markdown("""
    <style>
    .stButton>button { background-color: #28a745; color: white; border-radius: 8px; width: 100%; height: 50px; font-size: 18px; }
    .donate-btn { background-color: #ffdd00; color: black; padding: 12px; text-decoration: none; border-radius: 8px; font-weight: bold; display: block; text-align: center; margin-bottom: 20px; }
    .main { background-color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

# সাইডবার (Donation এবং Ads এর জন্য)
with st.sidebar:
    st.title("💰 Monetization")
    # নিচের লিঙ্কে আপনার নিজের 'Buy Me a Coffee' লিঙ্ক দিন
    st.markdown('<a href="https://www.buymeacoffee.com/yourusername" target="_blank" class="donate-btn">☕ Support me: Buy Me a Coffee</a>', unsafe_allow_html=True)
    st.write("---")
    st.info("📢 Ad Space: Google AdSense Placeholder")
    st.write("এই টুলটি ফ্রি রাখতে আমাদের সাপোর্ট করুন।")

# মেইন ইন্টারফেস
st.title("ProBrief AI 📝")
st.write("আপনার ক্লায়েন্ট মিটিংয়ের অডিও ফাইল আপলোড করুন এবং এক ক্লিকেই প্রফেশনাল সামারি ও অ্যাকশন আইটেম লিস্ট পান।")

# API Key এবং ফাইল ইনপুট
api_key = st.text_input("আপনার Gemini API Key এখানে দিন:", type="password")
uploaded_file = st.file_uploader("অডিও ফাইল সিলেক্ট করুন (MP3/WAV)", type=["mp3", "wav"])

if st.button("Generate Magic Summary ✨"):
    if uploaded_file and api_key:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner('এআই আপনার ফাইলটি প্রসেস করছে...'):
                # অডিও ডেটা রিড করা
                audio_data = uploaded_file.read()
                
                # প্রম্পট ইঞ্জিনিয়ারিং
                prompt = (
                    "You are a professional assistant for American freelancers. "
                    "Analyze this meeting audio and provide: "
                    "1. A concise summary of the discussion. "
                    "2. A clear bulleted list of Action Items (tasks to be done). "
                    "3. Key decisions made during the meeting."
                )
                
                response = model.generate_content([prompt, {"mime_type": "audio/mp3", "data": audio_data}])
                
                st.success("কাজ সম্পন্ন হয়েছে!")
                st.markdown("### ✅ Meeting Results")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"দুঃখিত, একটি সমস্যা হয়েছে: {e}")
    else:
        st.warning("দয়া করে অডিও ফাইল এবং API Key দুটিই প্রদান করুন।")

st.markdown("---")
st.caption("Privacy First: আমরা আপনার অডিও ফাইল সেভ করি না।")

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# --- Load environment variable (.env)
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- Inisialisasi model
model = genai.GenerativeModel("gemini-2.5-flash")

# --- Konfigurasi halaman Streamlit
st.set_page_config(page_title="AskMind AI Chatbot", page_icon="🤖", layout="centered")

# --- CSS kustom untuk gaya modern (💅)
st.markdown("""
    <style>
        .chat-container {
            max-width: 700px;
            margin: auto;
        }
        .user-msg, .bot-msg {
            border-radius: 15px;
            padding: 12px 16px;
            margin: 8px 0;
            line-height: 1.5;
        }
        .user-msg {
            background-color: #008000;
            text-align: right;
            margin-left: 20%;
            box-shadow: 0 1px 4px rgba(0,0,0,0.1);
        }
        .bot-msg {
            background-color: #333333;
            text-align: left;
            margin-right: 20%;
            box-shadow: 0 1px 4px rgba(0,0,0,0.1);
        }
        .chat-title {
            text-align: center;
            margin-bottom: 15px;
        }
        .reset-btn {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header
st.markdown("<h1 class='chat-title'>🤖 AskMind AI</h1>", unsafe_allow_html=True)
st.write("Chatbot Pengetahuan Umum berbasis Google Gemini")

# --- Tombol reset chat
st.markdown("<div class='reset-btn'>", unsafe_allow_html=True)
if st.button("🔁 Reset Chat"):
    st.session_state.messages = []
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# --- Simpan riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Container chat
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# --- Tampilkan riwayat pesan dengan gaya kartu
for msg in st.session_state.messages:
    role_class = "user-msg" if msg["role"] == "user" else "bot-msg"
    st.markdown(f"<div class='{role_class}'>{msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Input pengguna
if prompt := st.chat_input("Tanyakan sesuatu..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.spinner("Sedang berpikir..."):
        response = model.generate_content(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    st.rerun()
import streamlit as st
import requests, time
st.set_page_config(page_title="Bot Trading Ku", page_icon="🤖")
st.title("🤖 BOT TRADING KU")
st.write("Versi HP - Tinggal Klik START")
with st.sidebar:
    st.header("Setting Bot")
    api_key = st.text_input("API Key Indodax", type="password")
    secret_key = st.text_input("Secret Key", type="password")
    koin = st.selectbox("Pilih Koin", ["pepe_idr", "doge_idr", "shib_idr", "btc_idr", "eth_idr"])
    modal = st.number_input("Modal Per Beli (Rp)", value=25000)
    persen = st.number_input("Target Naik/Turun (%)", value=0.5)
    tombol_start = st.button("▶️ START BOT")
    tombol_stop = st.button("⏹️ STOP BOT")
if tombol_start:
    st.session_state.jalan = True
if tombol_stop:
    st.session_state.jalan = False
tempat_harga = st.empty()
tempat_status = st.empty()
def harga_sekarang(pair):
    r = requests.get(f"https://indodax.com/api/{pair}/ticker", timeout=10)
    return float(r.json()['ticker']['last'])
if st.session_state.get("jalan", False):
    st.success("Bot LAGI JALAN...")
    try:
        last = harga_sekarang(koin)
        tempat_harga.metric(label=f"Harga {koin.upper()}", value=f"Rp {last}")
        tempat_status.info(f"Modal: Rp {modal} | Target: {persen}% | Koin: {koin}")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("Bot lagi BERHENTI. Klik START di kiri buat jalanin.")
    try:
        last = harga_sekarang(koin)
        tempat_harga.metric(label=f"Harga {koin.upper()} (Pantau Saja)", value=f"Rp {last}")
    except:
        pass

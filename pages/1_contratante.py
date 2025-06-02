import streamlit as st

st.set_page_config(page_title="Contratar Artistas", layout="centered")

st.sidebar.title("📌 Menu")
st.sidebar.page_link("app.py", label="🔙 Página Inicial")
st.sidebar.markdown("Pesquise artistas com base no estilo e região.")

st.title("🔍 Buscar Artistas")

estilo = st.text_input("Qual estilo artístico você procura? (ex: samba, dança, stand-up...)")
local = st.text_input("Qual região? (ex: Rio de Janeiro, SP...)")

if st.button("🔎 Buscar"):
    st.info("Aqui apareceriam os artistas compatíveis com a busca. (função a ser implementada)")

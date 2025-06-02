import streamlit as st

st.set_page_config(page_title="StageUp", layout="centered")

st.title("🎭 StageUp")
st.subheader("Conectando artistas independentes com oportunidades ✨")

st.write("Seja bem-vindo à plataforma que valoriza talentos e conecta artistas com eventos em todo o Brasil.")
st.write("Escolha seu caminho abaixo:")

col1, col2 = st.columns(2)

with col1:
    if st.button("🎤 Sou Artista"):
        st.switch_page("pages/2_Artista.py")

with col2:
    if st.button("📋 Sou Contratante"):
        st.switch_page("pages/1_Contratante.py")
🧑‍💼 pages/1_Contratante.py (Página para contratantes)
python
Copiar
Editar
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

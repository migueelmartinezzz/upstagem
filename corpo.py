import streamlit as st

st.set_page_config(page_title="StageUp", layout="centered")

st.title("UPSTAGE")
st.subheader("Conectando artistas independentes com oportunidades")

st.write("Seja bem-vindo à plataforma que valoriza talentos e conecta artistas com eventos em todo o Brasil.")
st.write("Escolha seu caminho abaixo:")

col1, col2 = st.columns(2)

with col1:
    if st.button("Sou Artista"):
        st.switch_page("pages/2_Artista.py")

with col2:
    if st.button("Sou Contratante"):
        st.switch_page("pages/1_Contratante.py")


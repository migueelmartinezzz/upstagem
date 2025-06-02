import streamlit as st

st.set_page_config(page_title="Cadastro de Artistas", layout="centered")

st.sidebar.title("📌 Menu")
st.sidebar.page_link("app.py", label="🔙 Página Inicial")

st.title("🎤 Cadastro de Artistas Independentes")

with st.form(key="form_artista"):
    nome = st.text_input("Nome artístico")
    estilo = st.text_input("Estilo musical ou artístico (ex: MPB, dança contemporânea)")
    local = st.text_input("Cidade e estado onde atua")
    valor = st.text_input("Valor aproximado para eventos (ex: R$300, R$1000...)")
    descricao = st.text_area("Descrição sobre você, sua arte, seus diferenciais")
    imagem = st.file_uploader("Foto de divulgação", type=["jpg", "jpeg", "png"])

    enviar = st.form_submit_button("Cadastrar")

if enviar:
    st.success(f"Artista {nome} cadastrado com sucesso! 🎉")
    if imagem:
        st.image(imagem, caption=f"{nome}", use_column_width=True)


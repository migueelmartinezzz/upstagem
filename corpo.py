import streamlit as st

st.set_page_config(page_title="StageUp", layout="centered")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
        @font-face {
            font-family: 'Horizon';
            src: url('https://fonts.cdnfonts.com/s/80804/Horizon.woff') format('woff');
        }

        html, body, [class*="css"]  {
            font-family: 'Montserrat', sans-serif;
        }

        .title-container {
            text-align: center;
            padding: 2rem 1rem 1rem 1rem;
            border-bottom: 2px solid #cc0000;
        }

        .title-container h1 {
            font-family: 'Horizon', sans-serif;
            font-size: 4rem;
            color: #cc0000;
            margin-bottom: 0.5rem;
        }

        .button-container {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 2rem;
        }

        .stButton>button {
            font-size: 1rem !important;
            padding: 0.75rem 1.5rem !important;
            border-radius: 6px !important;
            font-weight: bold !important;
            border: none;
        }

        .artist-button button {
            background-color: #cc0000 !important;
            color: white !important;
        }

        .contractor-button button {
            background-color: #ffcc00 !important;
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

# Bloco do título e subtítulo
st.markdown("""
    <div class="title-container">
        <h1>UPSTAGE</h1>
        <p>Conectando artistas independentes com oportunidades</p>
        <p>Seja bem-vindo à plataforma que valoriza talentos e conecta artistas com eventos em todo o Brasil.</p>
    </div>
""", unsafe_allow_html=True)

# Botões centralizados
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="artist-button">', unsafe_allow_html=True)
    if st.button("🎤 Sou Artista"):
        st.switch_page("pages/2_Artista.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="contractor-button">', unsafe_allow_html=True)
    if st.button("📋 Sou Contratante"):
        st.switch_page("pages/1_Contratante.py")
    st.markdown('</div>', unsafe_allow_html=True)



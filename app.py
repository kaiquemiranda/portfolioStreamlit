import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import contato
import home
import skills
import projetos

# Carregar a imagem
img = Image.open('img/eu.png')

# Configuração da página
st.set_page_config(page_title="Kaique Miranda", page_icon=img, layout="wide")
st.sidebar.image('img/eu.png', width=240)
st.sidebar.markdown("<h1 style='color: white; text-align: left; font-size: 30px; margin-top: -20px; margin-bottom: 40px; margin-left: 40px;'>Kaique Miranda</h1>", unsafe_allow_html=True)
#st.sidebar.markdown("<h1 style='color: white; text-align: left; font-size: 20px; margin-top: -60px; margin-bottom: 40px; margin-left: 40px;'>Data science Analyst</h1>", unsafe_allow_html=True)

with open("style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Menu lateral
with st.sidebar:
    selecionado = option_menu(
        menu_title=None,
        options=["Sobre min", "Habilidades", "Projetos", "Contato"],
        icons=["file-person", "tools", "code-slash", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0c0c0c", "border-radius": "0px", "border-top": "2px white solid"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {"font-size": "25px", "color": "white", "text-align": "left", "margin": "0px", "--hover-color": "#rgb(0, 0, 0, 0.1)"},
            "nav-link-selected": {"background-color": "rgb(0, 0, 0, 0.1)"}
        }
    )


if selecionado == "Sobre min":
    home.inicio()

if selecionado == "Habilidades":
    skills.inicio()

if selecionado == "Projetos":
    projetos.inicio()

if selecionado == "Contato":
    st.markdown("<h1 style='color: #6f0909; text-align: center; font-size: 60px; margin-top: -80px; margin-bottom: 80px;'>Entre em contato</h1>", unsafe_allow_html=True)
    contato.social()
    contato.contact()


# Rodapé
st.markdown("<p style='text-align: center; margin-top: 200px; '> </p>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<p style='text-align: center;  font-size: 25px;'>Desenvolvido por Kaique Miranda - © 2024</p>", unsafe_allow_html=True)

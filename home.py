import json
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image



def get(path: str):
    with open(path, "r") as p:
        return json.load(p)

path = get("assets/Animation.json")
#path2 = get("assets/Cloud.json")

about = """Sou apaixonado por tecnologia e Análise de dados, com foco no uso de Python para resolver problemas complexos e gerar insights estratégicos.
Possuo conhecimento em bancos de dados SQL e NoSQL, além de experiência em desenvolvimento web. Estou sempre buscando aprender e aplicar novas tecnologias para transformar dados em valor para as empresas.
"""
unip = "Universidade Paulista (UNIP) | Análise e Desenvolvimento de Sistemas"
unip_text = " Durante minha graduação na UNIP, adquiri uma base sólida nos princípios de desenvolvimento de software e gestão de sistemas de informação. O curso me proporcionou conhecimento prático em linguagens de programação como C++, HTML, CSS, além de tecnologias relacionadas a bancos de dados SQL. A UNIP me preparou para lidar com desafios do mercado de TI, focando em soluções robustas e otimizadas para sistemas de software."
fiap_text = "Atualmente, estou cursando Ciência de Dados na FIAP, uma das instituições mais renomadas na área de tecnologia e inovação. O curso me permite aprofundar em áreas como machine learning, big data e análise avançada de dados. Além disso, desenvolvi habilidades em ferramentas como Python, Google Cloud, BigQuery e MongoDB, utilizando-as para análise, visualização e modelagem preditiva de dados. A FIAP tem me proporcionado uma abordagem prática e orientada ao mercado, preparando-me para enfrentar os desafios complexos do mundo dos dados."

def inicio():
    st.markdown("<h1 style=' color: #6f0909; text-align: center; font-size: 60px;  margin-top: -50px; margin-bottom: 80px;'>Hello friend</h1>", unsafe_allow_html=True)
    st.markdown(f"<h1 style=' text-align: center; font-size: 30px;  margin-top: -50px;'>{about}</h1>",unsafe_allow_html=True)
    st.markdown("----")

    st.markdown("<h1 style=' color: #6f0909; text-align: center; font-size: 60px;  margin-top: 140px; '>Formação academica</h1>", unsafe_allow_html=True)
    st.markdown("----")
    st.markdown("<h1 style=' color: #6f0909; text-align: center; font-size: 40px;  margin-top: 30px; margin-bottom: 80px;'>Análise e Desenvolvimento de Sistemas (UNIP)</h1>",unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('img/unip.jpg', width=400)
    with col2:
        st.markdown(f"<h1 style=' text-align: center; font-size: 25px;  margin-top: -40px; '>{unip_text}</h1>",
                    unsafe_allow_html=True)

    st.markdown("----")
    st.markdown(
        "<h1 style=' color: #6f0909; text-align: center; font-size: 35px;  margin-top: 20px; margin-bottom: 80px;'>Ciencia de dados (FIAP)</h1>",
        unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('img/fiap.jpg', width=400)
    with col2:
        st.markdown(f"<h1 style=' text-align: center; font-size: 25px;  margin-top: -70px;'>{fiap_text}</h1>",
                    unsafe_allow_html=True)


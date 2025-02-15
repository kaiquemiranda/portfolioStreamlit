import json
import streamlit as st
from streamlit_lottie import st_lottie



def get(path: str):
    with open(path, "r") as p:
        return json.load(p)

path = get("assets/Animation.json")
#path2 = get("assets/Cloud.json")
metheora = """O Metheora é uma plataforma que oferece informações meteorológicas em tempo real, previsões climáticas atualizadas e análises de riscos baseadas em inteligência artificial. A plataforma reúne dados de diversas fontes para fornecer insights detalhados sobre eventos climáticos extremos, como chuvas fortes e riscos de falta de energia, além de alertas de incidentes para regiões específicas. 
"""
analiseVendas = "Este projeto tem como objetivo analisar um relatório em Excel com dados de vendas do Mercado Livre, proporcionando insights estratégicos para a gestão de vendas e logística. A análise inclui a identificação de produtos com frete acima do valor desejado, os produtos mais vendidos com base em palavras-chave, além de cálculos da média de frete e a geração de relatórios detalhados de vendas."
dadoseducacionais = "Neste projeto, apliquei análise de dados em larga escala com Python, Pandas e SQL, realizando consultas otimizadas no Google BigQuery. Desenvolvi um dashboard interativo com Streamlit e Plotly, trazendo visualizações estratégicas sobre a infraestrutura das escolas no Brasil. Para enriquecer a experiência, integrei a API da OpenAI (ChatGPT), permitindo que o assistente virtual auxilie na análise e interpretação dos gráficos, tornando os insights mais acessíveis e compreensíveis. 🚀"


def inicio():
    st.markdown("<h1 style='color: #6f0909; text-align: center; font-size: 60px; margin-top: -80px;'>Projetos desenvolvidos</h1>", unsafe_allow_html=True)

    # ================================= PROJETO 1 =========================================================
    with st.container():
        st.markdown("----")

        st.markdown(
            "<h1 style=' color: #6f0909; text-align: right; font-size: 40px;  margin-top: 10px; margin-right: 25%; margin-bottom: 80px;'>Metheora</h1>",
            unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('img/metheora.png', width=400)
            st.markdown("Tecnologias Utilizadas: Python, Streamlit, MongoDB, Pandas, Numpy, Plotly, BeautifulSoup, Lottie Animation")
        with col2:
            st.markdown(f"<h1 style=' text-align: center; font-size: 25px;  margin-top: -80px; margin-left: 30px;'>{metheora}</h1>",
                        unsafe_allow_html=True)
            st.write("[Conheça o projeto](https://metheora.streamlit.app/)")

    # ================================= PROJETO 2 =========================================================
    with st.container():
        st.markdown("----")

        st.markdown(
            "<h1 style=' color: #6f0909; text-align: right; font-size: 40px;  margin-top: 0px; margin-right: 4%; margin-bottom: 80px;'>Análise de dados Educacionais</h1>",
            unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('img/inep.png', width=400)
            st.markdown("Tecnologias Utilizadas: Python, Streamlit, Pandas, Numpy, Plotly, OpenAI API, Google big Query")
        with col2:
            st.markdown(
                f"<h1 style=' text-align: center; font-size: 25px;  margin-top: -80px; margin-left: 30px;'>{dadoseducacionais}</h1>",
                unsafe_allow_html=True)
            st.write(
                "[Conheça o projeto](https://dadoseducacionais-inep.streamlit.app/)")

    # ================================= PROJETO 3 =========================================================
    with st.container():
        st.markdown("----")

        st.markdown(
            "<h1 style=' color: #6f0909; text-align: right; font-size: 40px;  margin-top: 0px; margin-bottom: 80px;'>Relatório de vendas Mercado livre</h1>",
            unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('img/dash.png', width=400)
            st.markdown("Tecnologias Utilizadas: Python, Streamlit, Pandas, Numpy, Plotly, excel")
        with col2:
            st.markdown(
                f"<h1 style=' text-align: center; font-size: 25px;  margin-top: -80px; margin-right: 2%; margin-left: 30px;'>{analiseVendas}</h1>",
                unsafe_allow_html=True)
            st.write(
                "[Conheça o projeto](https://dashboard-mercadolivre.streamlit.app/)")



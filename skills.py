import json
import streamlit as st
from streamlit_lottie import st_lottie



def get(path: str):
    with open(path, "r") as p:
        return json.load(p)

path = get("assets/Animation.json")
path2 = get("assets/dev.json")


def inicio():
    # Título da página
    st.markdown("<h1 style='color: #6f0909; text-align: center; font-size: 60px; margin-top: -80px;'>Habilidades Técnicas</h1>",
                unsafe_allow_html=True)
    st.markdown("----")

    # Lista de habilidades e porcentagens
    skills = {
        "Python": 0.90,
        "Pandas": 0.90,
        "Inglês": 0.80,
        "Plotly": 0.85,
        "MongoDB": 0.80,
        "excel": 0.70,
        "SQL": 0.70,
        "NoSQL": 0.85,
        "BigQuery": 0.45,
        "Google Cloud Storage": 0.45
    }

    col1, col2 = st.columns([2, 1])

    with col1:
        # Exibindo as habilidades com barras de porcentagem
        for skill, percent in skills.items():
            st.markdown(f"{skill}")
            st.progress(percent)
    with col2:
        st_lottie(path2, height=400, width=500)

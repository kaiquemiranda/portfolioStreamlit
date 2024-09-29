import json
import streamlit as st
from streamlit_lottie import st_lottie



def get(path: str):
    with open(path, "r") as p:
        return json.load(p)

path = get("assets/Animation.json")
#path2 = get("assets/Cloud.json")


def inicio():
    st.markdown("<h1 style=' text-align: center; font-size: 60px;  margin-top: -80px;'>Formação academica</h1>", unsafe_allow_html=True)
    st_lottie(path, height=600, width=1000)
    #st_lottie(path2, height=500, width=900)
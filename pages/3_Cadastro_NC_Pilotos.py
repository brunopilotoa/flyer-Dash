import streamlit as st
import pandas as pd
from inicio import file, base

st.title("Cadastro")
with st.form("piloto_cadastro_nc"):
    st.write("Formulario Para Pilotos")
    st.dataframe(base)

    st.form_submit_button(label="Cadastrar NC")

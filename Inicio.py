import pandas as pd

# import numpy as np
import streamlit as st
import plotly.express as px

## Titulo da Pagina e Layout Wide
st.set_page_config(page_title="Dashboard", layout="wide")
### Manipulacao dos Arquivos
# Nome do Arquivo Excel
file = "Base de Dados_Montagem Final_H23_2025.xlsx"
# Base de Dados
base = pd.read_excel(file, header=1)
# Base de Panes
panes = pd.read_excel(file, sheet_name="NCs_H23", header=1)

st.title("Bem vindo")
st.markdown("Aplicativo em Desenvolvimento")

st.divider()
## Insere 2 colunas no layout
col1, col2, col3 = st.columns(3)

with col1:
    #  Quantidade de Aeronaves em Montagem Final
    not_entregue = base[
        (base["STATUS FINAL"] != "ENTREGUE") & (base["Data VTI"] == "AGUARDANDO")
    ]
    not_entregue_counts = not_entregue["Prefixo"].value_counts().sum()
    st.metric(
        label="Aeronaves Em Processo" + "\n" + " De Montagem Final",
        value=not_entregue_counts,
    )


with col2:
    ## Quantidade das Aeronaves Entregues
    entregue = base[base["STATUS FINAL"] == "ENTREGUE"]
    entregue_counts = entregue["Prefixo"].value_counts().sum()
    st.metric(label="Aeronaves Entregues", value=entregue_counts)
with col3:
    meta = 40
    st.metric(
        label="Para Atingir a meta", value=meta - entregue_counts - not_entregue_counts
    )

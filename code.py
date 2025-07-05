import pandas as pd

# import numpy as np
import streamlit as st
import plotly.express as px

## Titulo da Pagina e Layout Wide
st.set_page_config(page_title="Dashboard V1.0", layout="wide")
### Manipulacao dos Arquivos
# Nome do Arquivo Excel
file = "Base de Dados_Montagem Final_H23_2025.xlsx"
# Base de Dados
base = pd.read_excel(file, header=1)
# Base de Panes
panes = pd.read_excel(file, sheet_name="NCs_H23", header=1)
## Insere a SideBar
#with st.sidebar:
#    st.title("Bem Vindo")
#    st.subheader("Graficos")
tab1,tab2=st.tabs(['Visao Geral','Por Aviao'])
with tab1:
    st.title("Visao Geral NCs")
    (col1, col2, ) = st.columns(2,gap='medium')
    with col1:
        # Figura que Mostra a Quantidade de Items por Setor AVI,GMP,CEL
        col1.fig = (
        px.bar(panes, x="Class NC", title="Quantidade de NC por Setor", )
        .update_xaxes(categoryorder="total descending", title="")
        .update_yaxes(title="Quantidade de NCs")
        )
        col1.fig.update_traces(width=0.3)
        col1.fig.update_layout(hovermode="x")
        st.plotly_chart(
        col1.fig,
    )

        ## Mais ocorridas
        nc = panes["Descrição da Não Conformidade"].value_counts()
        nc = nc[:10]
        col2.fig = (
            px.bar(nc, x="count", title="Mais Frequentes e Suas Quantias")
            .update_xaxes(
                title="",
            )
            .update_yaxes(categoryorder="total ascending", title="Quantidade")
        )
        st.plotly_chart(
            col2.fig,
        )

    with col2:
        ## Filtrando por Tipo de NC
        desc_nc = panes["Tipo NC"].value_counts()
        fig = (
            px.bar(
                desc_nc,
                title="Tipo de NC por Setor",
            )
            .update_xaxes(categoryorder="total descending", title="")
            .update_yaxes(title="Quantidade")
        )
        st.plotly_chart(fig, y="Tipo NC")
        fig2 = px.bar(panes, x="Prefixo", title='Ocorrencia por Aeronaves').update_yaxes(
            title='Quantidade').update_xaxes(title='Prefixo')
        st.plotly_chart(fig2, y="Prefixo")

with tab2:
    st.title('Por Aeronave')

    col1,col2 = st.columns(2,gap='large')

with col1:
    #cria o selectbox
    prefixo = st.selectbox(
        "",
        panes["Prefixo"].unique(),
        index=None,
        placeholder="Selecione a Aeronave",
    )
    st.subheader("NC em Aberto")
    #Filtra o dataset pelo selectbox
    panes_filtered = panes[panes["Prefixo"] == prefixo]
    opened_pane = panes_filtered[panes_filtered["Status"] != "Solucionado"]
    opened_pane["Descrição da Não Conformidade"]
    open_count = opened_pane["Prefixo"].value_counts()
    st.subheader("Quantidade " + f'{open_count.sum()}')
    #Cria o Grafico
    sector_panes = px.bar(panes_filtered, x="Class NC").update_xaxes(
        categoryorder="total descending", title='Setor'
    ).update_yaxes(title='Quantia')
    st.plotly_chart(sector_panes)

with col2:
    st.subheader("NC Concluidas")
    closed_pane = panes_filtered[panes_filtered["Status"] == "Solucionado"]
    closed_pane["Descrição da Não Conformidade"]
    st.write("Ultimas 5 Panes Reportadas")
    #st.write("Panes por Setor")

    last5 = panes_filtered[-5:]

    fig_last_5 = px.histogram(
        last5,
        y="Descrição da Não Conformidade",
    )
    st.plotly_chart(fig_last_5, title="Ultimas 5")


import pandas as pd
import numpy as np
import streamlit as st

# import plost
import plotly.express as px

base = pd.read_excel("Base de Dados_Montagem Final_H23_2025.xlsx", header=1)
panes = pd.read_excel(
    "Base de Dados_Montagem Final_H23_2025.xlsx", sheet_name="NCs_H23", header=1
)

lastpanes = panes[-10:]
st.set_page_config(layout="wide")

st.image(
    "https://static.wixstatic.com/media/683bd5_bdb5342d480b4d2188edd1c9373e8b74~mv2.png/v1/fill/w_622,h_176,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/683bd5_bdb5342d480b4d2188edd1c9373e8b74~mv2.png",
    width=300,
)
# st.title("Sistema  ")
# st.subheader("Dashboard Flyer")

## Aeronaves Entregues
# pd.to_datetime(base["Data Recebimento"])
# base["Data Recebimento"].dt.strftime("%d%m%Y")
entregue = base.loc[base["STATUS FINAL"] == "ENTREGUE"]
entregue.drop(columns=entregue.columns[0], axis=1, inplace=True)
# Limpeza
# st.header("Aeronaves ja Entregues")
# st.dataframe(entregue)


# st.subheader("VTI vs Entrega")
# plost.line_chart(entregue, y="Data VTI", x="Data de Entrega Cliente")

# st.subheader("Todas Aeronaves")
# drop first column
base.drop(columns=base.columns[0], axis=1, inplace=True)
# st.dataframe(base)
# st.header("Graficos VTI ")
# plost.line_chart(
#    base,
#    y="Prefixo",
#    x="Data VTI",
#    color="#1A5985",
#    title="Comparacao do Prefixo vs Data da VTI",
# )

fig = px.line(
    base,
    x="Data Recebimento",
    y="Data de Entrega Cliente",
    # color='Data  Cliente',
    text="Prefixo",
    markers=True,
    title="Gráfico Data de Recebimento e Entrega Cliente",
)
fig.update_traces(textposition="top left")


fig2 = px.bar(
    base,
    x="Data Recebimento",
    y="Data de Entrega Cliente",
    color="Prefixo",
    title="Data de Recebimento e VTI",
    text_auto=".2s",
)
fig2.update_traces(textfont_size=20, textangle=90)

fig3 = px.bar(panes, x="Class NC").update_xaxes(categoryorder="total ascending")
fig3.update_layout()

fig4 = px.histogram(
    lastpanes,
    y="Descrição da Não Conformidade",
)
fig5 = px.histogram(panes, y="Prefixo").update_yaxes(categoryorder="total ascending")
fig6 = px.histogram(panes, y="Descrição da Não Conformidade")
desc_nc=panes.iloc[:,10]
fig7=px.histogram(desc_nc,orientation='h')
fig7.update_layout(yaxis={'categoryorder':'total ascending'})

tab1, tab2, tab3 = st.tabs(["Graficos Gerais", "Panes", "Cadastros"])

with tab1:
    # col1, col2 = st.columns([3, 1])
    # with col1:
    #  st.header("Grafico 1")
    st.plotly_chart(fig)

    # with col2:
    # st.header("graf3")
    st.plotly_chart(fig2)

with tab2:
    # st.dataframe(panes)
    (
        col1,
        col2,
        col3,
        col4
    ) = st.columns(4)
    with col1:
        st.subheader("Ultimas 10 Panes Reportadas")
        st.plotly_chart(fig4)
    with col2:
        st.subheader("Panes por Setor")
        st.plotly_chart(fig3)
    with col3:
        st.subheader("Aeronave com Maiores Ocorrencias")
        st.plotly_chart(fig5)

        # st.subheader("Panes")
        # st.plotly_chart(fig6)
    with col4:
        st.subheader('Panes ')
        st.plotly_chart(fig7)
with tab3:
    st.subheader("Cadastro ")
    with st.form("aircraft"):
        numero = st.number_input("Numero ", min_value=0)
        pv = st.number_input("PV", min_value=0)
        prefixo = st.text_input("Prefixo")
        modelo = st.selectbox(
            "Escolha o Modelo da Aeronave",
            ("RV-10 LSA", "RV-12LSA", "RV-7", "Outros"),
            index=None,
            placeholder="Selecione a Aeronave...",
        )
        # N , PV , Prefixo , Modelo , Ns  MOtorizacao
        submitted = st.form_submit_button("Cadastrar")

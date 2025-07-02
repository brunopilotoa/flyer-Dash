import pandas as pd

# import numpy as np
import streamlit as st
import plotly.express as px

base = pd.read_excel("Base de Dados_Montagem Final_H23_2025.xlsx", header=1)
panes = pd.read_excel(
    "Base de Dados_Montagem Final_H23_2025.xlsx", sheet_name="NCs_H23", header=1
)

st.set_page_config(layout="wide")

url_logo = "https://static.wixstatic.com/media/683bd5_bdb5342d480b4d2188edd1c9373e8b74~mv2.png/v1/fill/w_622,h_176,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/683bd5_bdb5342d480b4d2188edd1c9373e8b74~mv2.png"
st.image(
    url_logo,
    width=300,
)
lastpanes = panes[-10:]
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


fig4 = px.histogram(
    lastpanes,
    y="Descrição da Não Conformidade",
)
fig5 = px.histogram(panes, y="Prefixo").update_yaxes(categoryorder="total ascending")
fig6 = px.histogram(panes, y="Descrição da Não Conformidade")

tab1, tab2, tab3, tab4 = st.tabs(["Graficos Gerais", "Panes", "Cadastros", "Aeronave"])

with tab1:
    (
        col1,
        col2,
    ) = st.columns([1, 3])
with col1:
    df_entregue = base[base["STATUS FINAL"] == "ENTREGUE"]
    anv_entregue = df_entregue["Prefixo"].value_counts()
    st.subheader("Aeronaves Entregues ")
    st.title(f"{anv_entregue.sum()}" + "\n Aeronaves LSA")
    #   col1, col2 = st.columns([4, 1])
    # with col1:

with col2:
    fig = px.bar(
        base,
        x="Data Recebimento",
        y="Data VTI",
        color="Prefixo",
        title="Data de Recebimento e VTI",
        text_auto=".2s",
    )
    fig.update_traces(
        textfont_size=40,
        # textangle=90
    )
    st.plotly_chart(fig)
    fig2 = px.line(
        base,
        x="Data VTI",
        y="Data de Entrega Cliente",
        # color='Data  Cliente',
        text="Prefixo",
        # markers=True,
        title="Data da VTI e Entrega ao Cliente",
        # trendline="ols",
    )
    fig2.update_traces(textposition="top left")

    st.plotly_chart(fig2)

    # st.subheader("Aeronaves Entregues")
    df_entregue = base[base["STATUS FINAL"] == "ENTREGUE"]
    # st.write(df_entregue)
    # fig_entregue = px.bar(df_entregue, y="Data de Entrega Cliente", x="Prefixo")
    # st.plotly_chart(fig_entregue)
with tab2:
    # st.dataframe(panes)
    (
        col1,
        col2,
        col3,
    ) = st.columns(3)
    with col1:
        st.write("Ultimas 10 Panes Reportadas")
        st.plotly_chart(fig4, title="Ultimas")
    with col2:
        st.write("Panes por Setor")
        fig3 = px.bar(panes, x="Class NC").update_xaxes(
            categoryorder="total descending"
        )
        fig3.update_layout()
        st.plotly_chart(fig3)
    with col3:
        st.write("Aeronave com Maiores Ocorrencias")
        st.plotly_chart(fig5)

        st.write("Panes")
        desc_nc = panes.iloc[:, 10]

        fig6 = px.histogram(desc_nc, orientation="h")
        fig6.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig6)
with tab3:
    st.subheader("Under Construction... ")
    # with st.form("aircraft"):
    # numero = st.number_input("Numero ", min_value=0)
    # pv = st.number_input("PV", min_value=0)
    # prefixo = st.text_input("Prefixo")
    # modelo = st.selectbox(
    # "Escolha o Modelo da Aeronave",
    # ("RV-10 LSA", "RV-12LSA", "RV-7", "Outros"),
    # index=None,
    # placeholder="Selecione a Aeronave...",
    # )
    # N , PV , Prefixo , Modelo , Ns  MOtorizacao
    # submitted = st.form_submit_button("Cadastrar")
with tab4:
    prefixo = st.selectbox("Selecione a Aeronave Abaixo", panes["Prefixo"].unique())
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("NC em Aberto")
        panes_filtered = panes[panes["Prefixo"] == prefixo]
        opened_pane = panes_filtered[panes_filtered["Status"] != "Solucionado"]
        opened_pane["Descrição da Não Conformidade"]
    with col2:
        st.subheader("NC Concluidas")
        closed_pane = panes_filtered[panes_filtered["Status"] == "Solucionado"]
        closed_pane["Descrição da Não Conformidade"]
        count_panes = panes_filtered[
            panes_filtered["Status"] == "Solucionado "
        ].value_counts()
        st.write(f"{count_panes.sum()} " + "Numero Total de Panes")

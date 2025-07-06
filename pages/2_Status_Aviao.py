import streamlit as st
from inicio import panes, px, base

tab1, tab2 = st.tabs(["Visao Geral", "Visao Detalhada"])
col1, col2 = st.columns(2)
with tab1:
    with col1:
        ## Bar das Aeronaves Entregues
        entregue = base[base["STATUS FINAL"] == "ENTREGUE"]
        entregue_counts = entregue["Prefixo"].value_counts().sum()
        fig_entregue = px.bar(
            entregue,
            y="Data de Entrega Cliente",
            x="Prefixo",
            title="Aeronaves Entregues",
        )
        st.metric(label="Aeronaves Entregues", value=entregue_counts)

        st.plotly_chart(fig_entregue)
    with col2:
        # Montagem Final
        not_entregue = base[
            (base["STATUS FINAL"] != "ENTREGUE") & (base["Data VTI"] == "AGUARDANDO")
        ]
        not_entregue_counts = not_entregue["Prefixo"].value_counts().sum()
        # data_vti=pd.to_datetime(data_vti).dt.strftime('%d/%m/%Y')

        fig_not_entregue = px.line(
            not_entregue,
            x="Data Recebimento",
            y="Prefixo",
            title="Aeronave em Processo de Montagem Final",
        )
        st.metric(
            label="Aeronaves Em Processo De Montagem Final", value=not_entregue_counts
        )
        st.plotly_chart(fig_not_entregue)

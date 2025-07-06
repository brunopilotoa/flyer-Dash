import streamlit as st
from inicio import panes, px, base

st.title("Visao Geral NCs H23")
tab1, tab2 = st.tabs(
    [
        "Graficos NC",
        "Por Aviao",
    ]
)
with tab1:
    (col1, col2, col3, col4) = st.columns(4)
    with col1:
        # Figura que Mostra a Quantidade de Items por Setor AVI,GMP,CEL
        col1.fig = (
            px.bar(
                panes,
                x="Class NC",
                title="Quantidade de NC por Setor",
            )
            .update_xaxes(categoryorder="total descending", title="")
            .update_yaxes(title="Quantidade de NCs")
        )
        col1.fig.update_traces(width=0.5)
        col1.fig.update_layout(hovermode="x")
        st.plotly_chart(
            col1.fig,
        )
    with col3:
        ## Filtrando por Tipo de NC
        desc_nc = panes["Tipo NC"].value_counts()
        fig2 = (
            px.bar(
                desc_nc,
                title="Tipo de NC por Setor",
                x="count",
            )
            .update_xaxes(title="Quantia  ")
            .update_yaxes(title="NC", categoryorder="total ascending")
        )
        st.plotly_chart(fig2, y="Tipo NC")
    with col2:
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
    with col4:
        fig3 = (
            px.bar(panes, y="Prefixo", title="Ocorrencia por Aeronaves")
            .update_yaxes(title="Quantidade", categoryorder="total ascending")
            .update_xaxes(title="Prefixo")
        )
        st.plotly_chart(fig3, y="Prefixo")
with tab2:
    # Cria o selectbox
    prefixo = st.selectbox(
        "",
        panes["Prefixo"].unique(),
        index=None,
        placeholder="Selecione a Aeronave",
    )
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.subheader("NC em Aberto")
        # Filtra o dataset pelo selectbox
        panes_filtered = panes[panes["Prefixo"] == prefixo]
        opened_pane = panes_filtered[panes_filtered["Status"] != "Solucionado"]
        st.dataframe(opened_pane["Descrição da Não Conformidade"])
    with col2:
        st.subheader("NC Concluidas")
        closed_pane = panes_filtered[panes_filtered["Status"] == "Solucionado"]
        closed_pane["Descrição da Não Conformidade"]
    with col3:
        # Cria o Grafico
        sector_panes = (
            px.bar(panes_filtered, x="Class NC", title="Quantidade Por Setor")
            .update_xaxes(categoryorder="total descending", title="Setor")
            .update_yaxes(title="Quantia")
        )
        st.plotly_chart(sector_panes)

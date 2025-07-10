import streamlit as st
from Inicio import panes, px, base,pd

tab1, tab2 = st.tabs(["Visao Geral", "Visao Detalhada"])
with tab1:
    col1, col2 = st.columns(2)
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

            ## Bar das Aeronaves Entregues
        entregue = base[base['STATUS FINAL']=='ENTREGUE']
        fig_entregue = px.bar(entregue, y="Data de Entrega Cliente", x="Prefixo",title='Aeronaves Entregues')
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
with tab2 :
    st.subheader('Aeronaves Entregue')
    select_aircraft = st.selectbox('',entregue['Prefixo'].unique(),index=None,placeholder="Selecione a Aeronave")
    entregue_filtered=entregue[entregue['Prefixo']==select_aircraft]
    anv_entregues=entregue_filtered[entregue_filtered['STATUS FINAL']=='ENTREGUE']
    recebimento_entregues=anv_entregues['Data Recebimento'].dt.strftime('%d/%m/%Y')
    vti=anv_entregues['Data VTI']
    vti=pd.to_datetime(vti).dt.strftime('%d/%m/%Y')
    #anv_entregues = pd.to_datetime(anv_entregues,dayfirst=False).dt.strftime('%d/%m/%Y')
    a,b=st.columns(2)
    b,c=st.columns(2)

    graph = anv_entregues[['Data Recebimento','Data VTI','Data de Entrega Cliente']]
    st.table(graph)

    #panes_filtered = panes[panes["Prefixo"] == prefixo]
    #opened_pane = panes_filtered[panes_filtered["Status"] != "Solucionado"]
    #st.dataframe(opened_pane["Descrição da Não Conformidade"])

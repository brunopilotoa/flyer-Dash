    df_entregue = base[base["STATUS FINAL"] == "ENTREGUE"]
    anv_entregue = df_entregue["Prefixo"].value_counts()
    st.subheader("Entregues ")
    st.subheader(f"{anv_entregue.sum()}" + " LSA")

    ## Aeronaves em VTI
    df_vti = base[base["Status VTI"] == "APROVADO"]
    anv_vistoriadas = df_vti["Prefixo"].value_counts()
    st.subheader("Vistoriadas")
    st.subheader(f"{anv_vistoriadas.sum()}" + " LSA")

    ## Anv IFR
    st.subheader("IFR Entregues")
    ifr_entregue = df_entregue[df_entregue["VFR/IFR"] == "IFR"]
    ifr_entregue = ifr_entregue["Prefixo"].value_counts()
    st.subheader(ifr_entregue.sum())
    st.subheader("VFR entregues")
    ## VFR entregues
    vfr_entregue = df_entregue[df_entregue["VFR/IFR"] != "IFR"]
    vfr_entregue = vfr_entregue["Prefixo"].value_counts()
    st.subheader(vfr_entregue.sum())



    st.subheader("Ultimas 10 Panes Reportadas")
    st.plotly_chart(fig4, user_container_width=True)
    # with col2:
    
    # with col3:
    st.write("Panes")
    desc_nc = panes.iloc[:, 10]

    fig6 = px.histogram(desc_nc, orientation="h")
    fig6.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig6)

    # col1, col2 = st.columns(
    #    2,
    # vertical_alignment="center"
    # )
    # with col1:

    #   with col2:
    st.subheader("NC Concluidas")
    closed_pane = panes_filtered[panes_filtered["Status"] == "Solucionado"]
    closed_pane["Descrição da Não Conformidade"]
    st.write("Ultimas 5 Panes Reportadas")
    #  closed_count = closed_pane["Prefixo"].value_counts()
    #        st.subheader(f"{closed_count.sum()} " + "Ocorrencias")




     with col1:
# with col2:
#    fig = px.bar(
#    base,
#    x="Data Recebimento",
#    y="Data VTI",
#    color="Prefixo",
#    title="Data de Recebimento e VTI",
#    text_auto=".2s",
# )
# fig.update_traces(textfont_size=40, textangle=90)
#  st.plotly_chart(fig)
# fig2 = px.line(
#    base,
#    x="Data VTI",
#    y="Data de Entrega Cliente",
# color='Data  Cliente',
#    text="Prefixo",
# markers=True,
#    title="Data da VTI e Entrega ao Cliente",
# trendline="ols",
# )
# fig2.update_traces(textposition="top left")

# st.plotly_chart(fig2)

# st.subheader("Aeronaves Entregues")
# st.write(df_entregue)

# st.dataframe(panes)
# (
#    col1,
#    col2,
#    col3,
# ) = st.columns(3, gap="large")
# with col1:



panes = pd.read_excel(
    "", sheet_name="NCs_H23", header=1
)



# url_logo = "https://static.wixstatic.com/media/683bd5_bdb5342d480b4d2188edd1c9373e8b74~mv2.png/v1/fill/w_622,h_176,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/683bd5_bdb5342d480b4d2188edd1c9373e8b74~mv2.png"
# st.image(
#    url_logo,
#    width=300,
# )
lastpanes = panes[-10:]

## Aeronaves Entregues

# fig6 = px.histogram(panes, y="Descrição da Não Conformidade")


(
    col1,
    col2,
) = st.columns(2)
#

# delivered = base[base["STATUS FINAL"] == "ENTREGUE"]
    # delivered_count = delivered["Prefixo"].value_counts()
    # delivered_count = delivered_count.sum()
    # st.header("Aeronaves Entregues \n" + f"{delivered_count}")
# with col2:
# st.title("Graficos")



        ## Bar das Aeronaves Entregues
        entregue = base[base['STATUS FINAL']=='ENTREGUE']
        fig_entregue = px.bar(entregue, y="Data de Entrega Cliente", x="Prefixo",title='Aeronaves Entregues')
        st.plotly_chart(fig_entregue)

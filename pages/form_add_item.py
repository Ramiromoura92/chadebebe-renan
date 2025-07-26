import streamlit as st
from models import Itens

right = st.columns(3)[0]
if right.button("Voltar para lista", icon=":material/mood:", use_container_width=True):
    st.switch_page("pages/lista_de_itens.py")

with st.form('dois'):
    
    st.write('<p style="color:white;">Adicionar item</p>', unsafe_allow_html=True)

    descricao = st.text_input('Adicionar item:')

    submitted = st.form_submit_button("Enviar")

    if submitted:
        if descricao.strip == "":
            print("Favor adicionar alguem item.")
        else:
            item = Itens(descricao)
            item.adicionar_item()
            st.success(f"Item '{descricao}' adicionado com sucesso!")

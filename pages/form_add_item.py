import streamlit as st
from models import Itens
from auth import verify_login


verify_login()

# Conteúdo protegido (só aparece se estiver logado)
right = st.columns(3)[0]
if right.button("Voltar para lista", icon=":material/mood:", use_container_width=True):
    st.switch_page("pages/lista_de_itens.py")


with st.form('dois'):
    
    st.write('<p style="color:#A67B5B;">Adicionar item</p>', unsafe_allow_html=True)

    descricao = st.text_input('Adicionar item:')

    submitted = st.form_submit_button("Enviar")

    if submitted:
        if descricao.strip() == "":
            st.warning("Favor adicionar algum item.")
        else:
            item = Itens()
            item.adicionar_item(descricao)
            st.success(f"Item '{descricao}' adicionado com sucesso!")
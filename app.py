import streamlit as st
from pages import form


pages = {

    
    "Formulário": [
        st.Page("pages/form.py", title='Preenha o formulário'),
    ],

    "Lista de confirmados": [
        st.Page("pages/lista_confirmacoes.py", title='Lista dos confirmados')
    ],

    "Lista de itens": [
        st.Page("pages/lista_de_itens.py", title='Lista de itens')
    ]
}

pg = st.navigation(pages, position='top')
pg.run()


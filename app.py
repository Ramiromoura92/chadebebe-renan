import streamlit as st

pages = {
    "Menu Principal": [  # seção
        st.Page("pages/form.py", title="Formulário"),
        st.Page("pages/lista_confirmacoes.py", title="Lista de Confirmados"),
        st.Page("pages/lista_de_itens.py", title="Lista de Itens"),
        st.Page("pages/form_add_item.py", title="Adicionar Item"),
    ]
}

pg = st.navigation(pages)
pg.run()



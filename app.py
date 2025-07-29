import streamlit as st

pages = {
    "Menu Principal": [  # seção
        st.Page("pages/form.py", title="Formulário"),
        st.Page("pages/lista_de_itens.py", title="Lista de Itens")
    ]
}

pg = st.navigation(pages)
pg.run()



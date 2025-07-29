import streamlit as st

pages = {
    "Menu Principal": [  # seção
        st.Page("pages/form.py", title="Confirmar presença"),
        st.Page("pages/lista_confirmacoes.py", title="Lista de Confirmados"),
        st.Page("pages/lista_de_itens.py", title="Lista de Mimos"),
        st.Page("pages/form_add_item.py", title="Adicionar Item"),
    ]
}

pg = st.navigation(pages)
pg.run()



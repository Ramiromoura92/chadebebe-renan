import streamlit as st
from models import PessoaDB, Itens


# CSS de fundo com responsividade
page_bg_img = """
<style>
body {
    margin: 0;
    padding: 0;
    min-height: 100vh;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: scroll; /* Melhor para mobile */
}

/* Transparência do app principal */
.stApp {
    background-color: rgba(0,0,0,0);
}

/* Ajustes para dispositivos móveis */
@media only screen and (max-width: 768px) {
    body {
        background-attachment: scroll;
        background-position: center center;
        background-size: cover;
    }
}
</style>
"""

# Aplica o estilo de fundo
st.markdown(page_bg_img, unsafe_allow_html=True)

# Título estilizado
st.markdown(
    '''
    <h1 style="
        color: white;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    ">
        Chá de Bebê do Renan
    </h1>
    ''',
    unsafe_allow_html=True
)


# Formulário
with st.form('form_renan'):
    st.write('<p style="color:white;">Por favor, confirme sua presença!</p>', unsafe_allow_html=True)

    name = st.text_input('Nome:')
    check = st.radio("Podemos contar com a sua presença?", ["Sim", "Não"])

    lista_opcoes = Itens.get_lista_itens()

    if lista_opcoes:
        choice = st.selectbox("O que pode levar?",lista_opcoes)
    else:
        st.warning("Nenhum item disponível para seleção.")
        choice = ""
    
    submitted = st.form_submit_button("Enviar")
    
    #Validação dos dados enviados
    if submitted:
        if name.strip() == "":

            print("Por gentileza, preencha o nome.")
        else:

            check_bool = check == "Sim" #Convertendo SIm/Não em boleando
            pessoa = PessoaDB(name,check,choice)
            pessoa.insert_data()
            
            if choice:
                Itens.remover_item_escolhido(choice)
                

                
            st.success("Dados enviados com sucesso! Obrigado, Renan agradeçe!")


# CSS para o formulário
css = """
<style>
    [data-testid="stForm"] {
        background-color: rgba(0, 0, 0, 0.5);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
    }

    /* Ajusta cor do texto dos inputs */
    label, .stTextInput label, .stNumberInput label, .stRadio label {
        color: white !important;
    }

    /* Ajusta inputs para fundo escuro */
    input, textarea {
        background-color: #ffffffdd !important;
        color: black !important;
    }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Resultado após envio
if submitted:
    st.success("Obrigado pela confirmação!")

import streamlit as st
from models import PessoaDB, Itens, Acompanhante


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
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">

    <div style="
        font-family: 'Dancing Script', cursive;
        color: white;
        text-align: center;
        padding: 1em;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    ">
        <h1 style="font-size: 3em; margin-bottom: 0.5em;">Chá de Bebê do Renan</h1>
        <h2 style="font-size: 1.5em; line-height: 1.6;">
            "Era este menino que eu pedia, e o Senhor concedeu-me o pedido."<br>
            "Por isso, agora, eu o dedico ao Senhor. Por toda a sua vida será dedicado ao Senhor."<br>
            — 1 Samuel 1:27-28
        </h2>
    </div>
""", unsafe_allow_html=True)




# Formulário
# Formulário
with st.form('formulario_confirmacao'):
    st.markdown('<p style="color:white;">Por favor, confirme sua presença!</p>', unsafe_allow_html=True)

    name = st.text_input('Nome:')
    check = st.radio("Podemos contar com a sua presença?", ["Sim", "Não"])
    check_2 = st.radio("Acompanhante?", ["Sim", "Não"], index=0)
    
    if check_2 == "Sim":
        company = st.text_input("Nome do(s) acompanhante(s): ")
    else:
        company = None
    
    itens = Itens()
    lista_opcoes = itens.get_lista_itens()

    if lista_opcoes:
        choice = st.selectbox("O que pode levar?", lista_opcoes)
    else:
        st.warning("Nenhum item disponível para seleção.")
        choice = ""
    
    submitted = st.form_submit_button("Enviar")
    
    if submitted:
        if name.strip() == "":
            st.warning("Por gentileza, preencha o nome.")
            
        elif check_2 == "Sim" and (not company or company.strip() == ""):
            st.warning("Por favor, informe o(s) nome(s) do(s) acompanhante(s).")

        else:
            check_bool = check == "Sim"
            pessoa = PessoaDB(name, check, choice)
            pessoa_id = pessoa.insert_data()

            # Apenas insere acompanhante se for necessário
            if check_2 == "Sim" and company:
                companhia = Acompanhante(company, pessoa_id)
                companhia.insert_data()

            if choice:
                item = Itens()
                item.remover_item_escolhido(choice)

            st.success("Dados enviados com sucesso! Obrigado, Renan agradece!")



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

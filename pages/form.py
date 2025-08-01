import streamlit as st
from models import PessoaDB, Itens, Acompanhante

# CSS completo
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap');

body {
    background-image: url("https://i.imgur.com/ZKrI7oa.jpeg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

.stApp {
    background-color: rgba(255, 255, 255, 0.92);
    color: #5C4033;
    font-family: 'Segoe UI', sans-serif;
}

h1, h2, h3, h4, h5, h6, label, .stRadio > label, .stTextInput > label {
    color: #5C4033;
}

input, textarea, select {
    background-color: #FFF9F3 !important;
    color: #5C4033 !important;
    border-radius: 8px !important;
    font-size: 1rem !important;
}

/* Botões */
.stButton > button {
    background-color: #A67B5B;
    color: white;
    border: none;
    padding: 0.5rem 1.2rem;
    border-radius: 8px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #8B5E3C;
}

/* Selectbox dropdown corrigido */
.stSelectbox > div > div {
    background-color: #FFF9F3 !important;
    color: #5C4033 !important;
}

/* Form container */
.form-container {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 2rem;
    border-radius: 15px;
    max-width: 600px;
    margin: 2rem auto;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}
"""

# Aplica o CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Título estilizado com versículo
st.markdown("""
    <div style="
        font-family: 'Dancing Script', cursive;
        color: #A67B5B;
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
        <h3>
            Venha comemorar conosco nesse dia tão especial! <br>
            Data: 13 de setembro às 12:00 <br>
            Local: Espaço Casa Amarela 
                   Rua Gramado,653-Campo Grande, RJ 
        </h3>

            
    </div>
""", unsafe_allow_html=True)

# Título
st.markdown('<p style="color:#A67B5B; text-align:center; font-size:24px;">Por favor, confirme sua presença!</p>', unsafe_allow_html=True)

# Entrada de dados
name = st.text_input('Nome:')
check = st.radio("Podemos contar com a sua presença?", ["Sim", "Não"])

# Inicialização
company = None
choice = ""
check_2 = "Não"

# Se confirmou presença
if check == "Sim":
    check_2 = st.radio("Acompanhante?", ["Sim", "Não"], index=0)

    if check_2 == "Sim":
        company = st.text_input("Nome do(s) acompanhante(s):")

    itens = Itens()
    lista_opcoes = itens.get_lista_itens()

    if lista_opcoes:
        choice = st.selectbox("Escolha um mimo para o Renan:", options=lista_opcoes,format_func=lambda x: x[1])
    else:
        st.warning("Nenhum item disponível para seleção.")
        choice = ""

    # Formulário com container estilizado
    with st.form("formulario_confirmacao"):
        submitted = st.form_submit_button("Enviar")

        if submitted:
            if name.strip() == "":
                st.warning("Por gentileza, preencha o nome.")
            elif check_2 == "Sim" and (not company or company.strip() == ""):
                st.warning("Por favor, informe o(s) nome(s) do(s) acompanhante(s).")
            else:
                pessoa = PessoaDB(name, 1, choice)
                pessoa_id = pessoa.insert_data()

                if check_2 == "Sim" and company:
                    companhia = Acompanhante(company, pessoa_id)
                    companhia.insert_data()

                if choice:
                    item = Itens()
                    item.remover_item_escolhido(choice)

                st.success("Dados enviados com sucesso! Obrigado, Renan agradece!")

# Se não confirmou presença
else:
    print(check)
    with st.form("formulario_confirmacao"):
        submitted = st.form_submit_button("Enviar")

        if submitted:
            if name.strip() == "":
                st.warning("Por gentileza, preencha o nome.")
            else:
                pessoa = PessoaDB(name, 0, choice)
                pessoa.insert_data()
                st.success("Sua resposta foi registrada. Obrigado!")
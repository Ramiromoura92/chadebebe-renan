import streamlit as st
from models import Itens




# Usuários autorizados
USUARIOS = {
    "RamiroSilva": "Ramo@10110",
    "RaianeLima": "Raiane@10110"
}

# Função de login
def login():
    st.title("Faça o login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            st.session_state['logado'] = True
            st.session_state['usuario'] = usuario
            st.success(f"Bem-vindo, {usuario}!")
        else:
            st.error("Usuário ou senha incorretos")

# Verifica se o usuário está logado
if 'logado' not in st.session_state or not st.session_state['logado']:
    login()
    st.stop()  # Interrompe o restante da execução se não estiver logado

# Conteúdo protegido (só aparece se estiver logado)
right = st.columns(3)[0]
if right.button("Voltar para lista", icon=":material/mood:", use_container_width=True):
    st.switch_page("pages/lista_de_itens.py")

with st.form('dois'):
    st.write('<p style="color:white;">Adicionar item</p>', unsafe_allow_html=True)

    descricao = st.text_input('Adicionar item:')

    submitted = st.form_submit_button("Enviar")

    if submitted:
        if descricao.strip() == "":
            st.warning("Favor adicionar algum item.")
        else:
            item = Itens(descricao)
            item.adicionar_item()
            st.success(f"Item '{descricao}' adicionado com sucesso!")
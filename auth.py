import streamlit as st

def get_usuarios():
    return dict(st.secrets["usuarios"])

def login():
    st.title("Faça o login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        usuarios = get_usuarios()
        if usuario in usuarios and usuarios[usuario] == senha:
            st.session_state['logado'] = True
            st.session_state['usuario'] = usuario
            st.success(f"Bem-vindo, {usuario}!")
        else:
            st.error("Usuário ou senha incorretos")


def verify_login():
    if 'logado' not in st.session_state or not st.session_state['logado']:
        login()
        st.stop()  # Interrompe o restante da execução se não esti
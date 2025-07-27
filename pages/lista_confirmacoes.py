from supabase import create_client
import streamlit as st
import pandas as pd

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

SUPABASE_URL = "https://afcvlygdllpqbkehqjmf.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFmY3ZseWdkbGxwcWJrZWhxam1mIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzU2MTQwMiwiZXhwIjoyMDY5MTM3NDAyfQ.taSe9z5L7cxGsqv1dlgE4SZqZG3BmBuCatjVb9DcRAY"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Função para buscar os dados do banco
def get_all_pessoas():

    response_pessoas = supabase.table("pessoas").select("*").execute()
    pessoas = response_pessoas.data

    response_companhia = supabase.table("companhia").select("nome, pessoa_id").execute()
    companhias = response_companhia.data

     # Junta os dados manualmente (simulando LEFT JOIN)
    dados = []
    for p in pessoas:
        pessoa_id = p["id"]
        nome_pessoa = p["nome"]
        check_value = p["check_value"]
        choice = p["choice"]

        # Filtra acompanhantes da pessoa
        acompanhante = ", ".join([c["nome"] for c in companhias if c["pessoa_id"] == pessoa_id]) or None

        dados.append({
            "Id": pessoa_id,
            "Nome": nome_pessoa,
            "Presença": "Sim" if check_value else "Não",
            "Item": choice,
            "Acompanhante(s)": acompanhante
        })

    df = pd.DataFrame(dados)
    return df


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
    <h2 style="
        color: white;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    ">

    Confirmados!

    </h2> 
    ''',
    unsafe_allow_html=True
)
# Interface Streamlit

df_pessoas = get_all_pessoas()

if not df_pessoas.empty:
    st.table(df_pessoas)
else:
    st.info("Nenhum dado encontrado no banco ainda.")

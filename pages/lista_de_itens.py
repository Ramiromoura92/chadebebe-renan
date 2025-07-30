from supabase import create_client
import streamlit as st
import pandas as pd

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

right = st.columns(3)[0]
if right.button("Adicionar um novo item", icon=":material/mood:", use_container_width=True):
    st.switch_page("pages/form_add_item.py")

# Função para buscar os dados do banco
def get_all_itens():
    try:
        response = supabase.table("lista_itens").select("descricao").execute()
        dados = response.data

        if not dados:
            return pd.DataFrame(columns=["descricao"])
        
        df = pd.DataFrame(dados)  # Supabase já retorna lista de dicionários
        return df

    except Exception as e:
        st.error(f"Erro ao buscar itens: {e}")
        return pd.DataFrame(columns=["descricao"])

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
        color: #A67B5B;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    ">
        Lista de mimos 
        
    </h1>
    ''',
    unsafe_allow_html=True
)
# Interface Streamlit


df_itens = get_all_itens()

if not df_itens.empty:
    st.table(df_itens)
else:
    st.info("Nenhum dado encontrado no banco ainda.")

import sqlite3
import streamlit as st
import pandas as pd

# Função para buscar os dados do banco
def get_all_pessoas():
    conn = sqlite3.connect('chadebebe.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nome, check_value, choice FROM pessoas")
    dados = cursor.fetchall()
    conn.close()

    # Transformar em DataFrame para exibir como tabela
    df = pd.DataFrame(dados, columns=["Nome", "Presença", "Item"])

    # Converte valor booleano de volta para texto
    df["Presença"] = df["Presença"].apply(lambda x: "Sim" if x == 1 else "Não")
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

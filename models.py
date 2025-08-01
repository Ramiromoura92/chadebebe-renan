from supabase import create_client, Client
import streamlit as st

class PessoaDB:
    def __init__(self, nome, check, choice):
        self.nome = nome
        self.check = bool(check)
        self.choice = choice
        self.url = st.secrets["SUPABASE_URL"]
        self.key = st.secrets["SUPABASE_KEY"]
        self.supabase = create_client(self.url, self.key)

    def insert_data(self):
        data = {
            "nome": self.nome,
            "check_value": int(self.check),
            "choice": self.choice
        }

        try:
            response = self.supabase.table("pessoas").insert([data]).execute()
            pessoa_id = response.data[0]["id"]
            print(f'Dado inserido: {response.data}')
            return pessoa_id  # geralmente retorna uma lista com um dicionário
        except Exception as e:
            print("Erro ao inserir:", e)
            return None
   
class Itens:
    def __init__(self):
        self.url = "https://afcvlygdllpqbkehqjmf.supabase.co"  # substitua pela sua URL
        self.key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFmY3ZseWdkbGxwcWJrZWhxam1mIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzU2MTQwMiwiZXhwIjoyMDY5MTM3NDAyfQ.taSe9z5L7cxGsqv1dlgE4SZqZG3BmBuCatjVb9DcRAY"                # substitua pela sua anon key
        self.supabase = create_client(self.url, self.key)

    def adicionar_item(self, descricao):
        data = {"descricao": descricao}
        try:
            response = self.supabase.table("lista_itens").insert([data]).execute()
            print("Item adicionado:", response.data)
            return response.data
        except Exception as e:
            print("Erro ao adicionar item:", e)
            return None

    def get_lista_itens(self):
        try:
            response = self.supabase.table("lista_itens").select("*").execute()
            #import ipdb; ipdb.set_trace()
            return [(item["id"],item["descricao"]) for item in response.data]
        except Exception as e:
            print("Erro ao buscar itens:", e)
            return []

    def remover_item_escolhido(self, item):
        try:
            response = self.supabase.table("lista_itens").delete().eq("id", item[0]).execute()
            print("Item removido:", item[1])
            return True
        except Exception as e:
            print("Erro ao remover item:", e)
            return False


class Acompanhante:
    def __init__(self, nome, pessoa_id):
        self.nome = nome
        self.pessoa_id = pessoa_id

        self.url = "https://afcvlygdllpqbkehqjmf.supabase.co"  # substitua pela sua URL
        self.key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFmY3ZseWdkbGxwcWJrZWhxam1mIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MzU2MTQwMiwiZXhwIjoyMDY5MTM3NDAyfQ.taSe9z5L7cxGsqv1dlgE4SZqZG3BmBuCatjVb9DcRAY"# substitua pela sua anon key                # sua anon key
        self.supabase = create_client(self.url, self.key)

    def insert_data(self):
        data = {
            "nome": self.nome,
            "pessoa_id": int(self.pessoa_id)  # Garantir que seja int
        }

        try:
            response = self.supabase.table("companhia").insert([data]).execute()
            print("Acompanhante inserido:", response.data)
            return response.data
        except Exception as e:
            print("Erro ao inserir acompanhante:", e)
            return None

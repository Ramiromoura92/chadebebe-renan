import sqlite3
import os

class PessoaDB:
    def __init__(self, nome, check, choice):
        self.nome = nome
        self.check = bool(check)
        self.choice = choice

        self.db_name = 'chadebebe.db'
        self.conn = self.create_connection()
        self.create_table()

    def create_connection(self):
        
        db_exists = os.path.exists(self.db_name)
        conn = sqlite3.connect(self.db_name)
        if db_exists:
            print("Banco de dados já existe.")
        else:
            print("Banco de dados criado.")
        return conn


    def create_table(self):
        
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                check_value INTEGER NOT NULL,  -- Booleano representado como inteiro (0 ou 1)
                choice TEXT
            )
        """)
        self.conn.commit()

    def insert_data(self):
        
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO pessoas (nome, check_value, choice)
            VALUES (?, ?, ?)
        """, (self.nome, int(self.check), self.choice))
        self.conn.commit()
        print(f'Dado inserido: {self.nome}, {self.check}, {self.choice}')
    
   
class Itens:

    def __init__(self,descricao,nome):
        
            self.descricao = descricao
            self.nome = nome

            self.db_name = 'chadebebe.db'
            self.conn = self.create_connection()
            self.create_table() 
            
    def create_connection(self):
        
        db_exists = os.path.exists(self.db_name)
        conn = sqlite3.connect(self.db_name)
        if db_exists:
            print("Banco de dados já existe.")
        else:
            print("Banco de dados criado.")
        return conn

    
    def get_lista_itens():
        conn = sqlite3.connect('chadebebe.db')
        cursor = conn.cursor()
        cursor.execute("SELECT DESCRICAO FROM lista_itens")
        itens = [row[0] for row in cursor.fetchall()]
        conn.close()
        return itens
    
    def remover_item_escolhido(descricao):
        conn = sqlite3.connect('chadebebe.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM lista_itens WHERE descricao = ?", (descricao,))
        conn.commit()
        conn.close()
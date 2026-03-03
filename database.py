import sqlite3
import pandas as pd

def criar_conexao():
    return sqlite3.connect('vendas.db')

def criar_tabelas():
    conn = criar_conexao()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gerentes(
            id_gerente INTEGER PRIMARY KEY,
            nome_gerente VARCHAR(20),
            loja VARCHAR(10)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas(
            id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
            data_venda VARCHAR(10),
            produto VARCHAR(20),
            quantidade INTEGER,
            preco_unitario REAL,
            valor_total REAL,
            id_gerente INTEGER,
            FOREIGN KEY (id_gerente) REFERENCES gerentes (id_gerente)
        )
    ''')
    
    conn.commit()
    conn.close()

def carga(df_vendas, df_gerentes):
    conn = criar_conexao()
    df_gerentes.to_sql('gerentes', conn, if_exists='replace', index=False)
    df_vendas.to_sql('vendas', conn, if_exists='replace', index=False)
    conn.close()
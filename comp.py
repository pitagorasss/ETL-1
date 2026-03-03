import pandas as pd

VENDAS_PATH = '/home/pitagoras/Área de trabalho/ETL/ETL-1/dados/vendas.csv'
GERENTES_PATH = '/home/pitagoras/Área de trabalho/ETL/ETL-1/dados/gerentes.xlsx'
# /////////// Extração ///////////////////////////
def extracao(vendas: str = VENDAS_PATH, gerentes: str = GERENTES_PATH, low_memory=False):
    df_vendas = pd.read_csv(vendas, low_memory=low_memory)
    df_gerentes = pd.read_excel(gerentes)
    return df_vendas, df_gerentes

# /////////// Transformação //////////////////////
def transformacao(df_vendas, df_gerentes, low_memory=False):
    df_vendas = df_vendas.drop(columns=['DATA_BASE']) # === Excluir coluna DATA_BASE
    df_vendas['LOJA'] = df_vendas['LOJA'].fillna('Online') # === Preencher com "Online" as linhas vazias da coluna 'LOJA'
    df_vendas = df_vendas.dropna() # === Excluir linhas com valores nulos
    df_vendas['DATA'] = pd.to_datetime(df_vendas['DATA'], format="%Y-%m-%d").dt.date # === Formatação de data e remoção da hora, pois não há o horário no banco de dados de extração
    df_vendas = df_vendas.drop_duplicates(subset=['ID'], keep='first') # === Remove linhas duplicadas da coluna "ID" mantendo o primeiro registro ([keep='False'] remove todas as duplicatas e [keep='last'] mantém a última)
    df_vendas['LOJA'] = df_vendas['LOJA'].str.strip() # Padroniza formatação dos nomes das lojas retirando espaços antes e depois do nome da loja
    df_vendas['LOJA'] = df_vendas['LOJA'].str.title() # "                                      " deixando a inicial de cada palavra em maiúsculo (ex.: "São Paulo" e não "'São paulo' ou 'são paulo'")
    return df_vendas, df_gerentes
    
    
    
    
    df_gerentes["Loja"] = df_gerentes["Loja"].str.strip()
    df_gerentes["Loja"] = df_gerentes["Loja"].str.title()
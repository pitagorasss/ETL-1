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
    df_vendas['DATA'] = pd.to_datetime(df_vendas['DATA'], format="%Y-%m-%d") # === Formatação de data
    df_vendas = df_vendas.drop_duplicates(subset=['ID'], keep='first') # === Remove linhas duplicadas da coluna "ID" mantendo o primeiro registro ([keep='False'] remove todas as duplicatas e [keep='last'] mantém a última)

    



    print(df_vendas)
    return df_vendas, df_gerentes
    
    
    
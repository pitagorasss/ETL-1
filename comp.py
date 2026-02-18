import pandas as pd

VENDAS_PATH = '/home/pitagoras/Área de trabalho/ETL/ETL-1/dados/vendas.csv'
GERENTES_PATH = '/home/pitagoras/Área de trabalho/ETL/ETL-1/dados/gerentes.xlsx'
# /////////// Extração ///////////////////////////
def extracao(vendas: str = VENDAS_PATH, gerentes: str = GERENTES_PATH, low_memory=False):
    df_vendas = pd.read_csv(vendas)
    df_gerentes = pd.read_excel(gerentes)
    return df_vendas, df_gerentes

# /////////// Transformação //////////////////////
def transformacao(df_vendas, df_gerentes, low_memory=False):
    df_vendas = df_vendas.drop(columns=['DATA_BASE']) # === Excluir coluna DATA_BASE
    df_vendas['LOJA'] = df_vendas['LOJA'].fillna('Online') # Preencher com "Online" as linhas vazias da coluna 'LOJA'
    df_vendas = df_vendas.dropna() # Excluir linhas com valores nulos
    df_vendas['DATA'] = pd.to_datetime(df_vendas['DATA'], format="%Y-%m-%d") # Formatação de data
    print(df_vendas.shape)
    return df_vendas, df_gerentes
    
    


import pandas as pd
import numpy as np
from pathlib import Path
from comp import extracao, transformacao
from database import criar_tabelas, carga

def etl():
    df_vendas, df_gerentes = extracao(low_memory=False)
    df_vendas, df_gerentes = transformacao(df_vendas, df_gerentes, low_memory=False)
    criar_tabelas()
    carga(df_vendas, df_gerentes)
    
    return df_vendas, df_gerentes
     
if __name__ == '__main__':
    df_vendas, df_gerentes = etl()
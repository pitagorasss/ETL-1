# 📊 Pipeline de Dados • ETL • Vendas • Gestão Comercial

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.3.3-green)
![SQLite](https://img.shields.io/badge/SQLite-3-blue)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-3.1.2-orange)

## 🎯 Visão Geral

Este projeto implementa um fluxo ETL (Extract, Transform, Load) completo para processamento de dados comerciais:

- **Extrai** dados de vendas (CSV) e gerentes (Excel)
- **Transforma** aplicando regras de limpeza, padronização de datas, tratamento de valores nulos e remoção de duplicatas
- **Carrega** em banco SQLite com integridade relacional garantida

O objetivo é fornecer uma base de dados confiável e pronta para análises de desempenho comercial.

---

## ❗ Problema

Os dados brutos de vendas e gerentes encontram-se em formatos distintos (CSV e Excel) e apresentam diversas inconsistências:

| Problema | Impacto |
|----------|---------|
| **Valores nulos** em colunas importantes (ex.: `LOJA`) | Dados incompletos para análise |
| **Datas com formatação incorreta** e horários desnecessários | Dificuldade em análises temporais |
| **Registros duplicados** baseados em `ID` | Distorção de métricas e contagens |
| **Falta de integridade relacional** entre vendas e gerentes | Impossibilidade de análises conjuntas |

Esses problemas comprometem a qualidade e a confiabilidade das análises de desempenho de vendas por gerente, região ou produto.

---

## ✅ Solução

Foi desenvolvido um pipeline ETL em Python utilizando a biblioteca **Pandas** para:

### 📤 Extração
- Leitura automatizada de `vendas.csv` com `pd.read_csv()`
- Leitura automatizada de `gerentes.xlsx` com `pd.read_excel()`
- Tratamento de encoding e baixo consumo de memória

### 🔄 Transformação
- **Remoção de colunas irrelevantes**: exclusão da coluna `DATA_BASE`
- **Tratamento de valores nulos**: 
  - Preenchimento de `LOJA` com "Online" quando vazio
  - Exclusão de linhas com qualquer outro valor nulo
- **Padronização de datas**: conversão para `YYYY-MM-DD` com remoção de horários
- **Deduplicação**: remoção de registros duplicados baseada no campo `ID` (mantém o primeiro)
- **Cálculo de métricas**: criação da coluna `valor_total` (quantidade × preço_unitário)

### 💾 Carga
- Criação automática das tabelas `gerentes` e `vendas` no SQLite
- Estabelecimento de relacionamento por chave estrangeira (`id_gerente`)
- Inserção dos dados processados com `df.to_sql()`

---

## 📈 Resultado

✅ **Base única e consistente** – sem duplicatas e com datas padronizadas  

✅ **Dados prontos para consumo** – compatível com SQLite, PostgreSQL, MySQL e qualquer outro outro banco relacional
✅ **Qualidade garantida** – 100% dos registros tratados e validados  

✅ **Análises confiáveis** – Informações precisas de performance de vendas por gerente, região e produto  

✅ **Processo automatizado** – execução simples com um comando  



## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Função |
|------------|--------|--------|
| **Python** | 3.14+ | Linguagem base |
| **Pandas** | 2.3.3 | Manipulação e transformação de dados |
| **SQLite3** | nativa | Banco de dados relacional |
| **OpenPyXL** | 3.1.2 | Leitura de arquivos Excel |
| **NumPy** | 1.26+ | Suporte a operações numéricas |
| **PathLib** | nativa | Gerenciamento de caminhos |

---

## 📁 Estrutura do Projeto
ETL-1/


                ├── 📄 ETL.py # Orquestrador principal do pipeline
                ├── 📄 comp.py # Funções de extração e transformação
                ├── 📄 database.py # Funções de conexão e carga no SQLite
                ├── 📄 vendas.db # Banco de dados gerado (após execução)
                │
                └── 📁 dados/ # Pasta para os arquivos de entrada
                ├── 📄 vendas.csv # Dados brutos de vendas (obrigatório)
                └── 📄 gerentes.xlsx # Dados brutos de gerentes (obrigatório)
                └── 📄 README.md # Documentação
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///meubanco.db")

# --- Leitura da Planilha Excel (Aba: VE-DO) ---
try:
    df_imoveis = pd.read_excel(
        "cadastro_aliança.xlsx",
        sheet_name="VE-DO",
        skiprows=[0],
        usecols="A:G",
        header=1
    )
    print("Aba 'VE-DO' lida com sucesso!")
except FileNotFoundError:
    print("Erro: O arquivo 'cadastro_aliança.xlsx' não foi encontrado.")
    exit()

# Mapeamento para a tabela 'imoveis'
mapeamento_imoveis = {
    'SITUAÇAO': 'status',
    'CONTATO': 'fone',
    'IMÓVEL': 'tipo',
    'DR': 'data_registro',
    'PROPRIT': 'proprietario'
}
df_imoveis = df_imoveis.rename(columns=mapeamento_imoveis)
df_imoveis.to_sql('imóveis', con=engine, if_exists='append', index=False)
print("Dados de imóveis importados para o banco de dados com sucesso!")
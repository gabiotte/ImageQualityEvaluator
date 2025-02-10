import pandas as pd
import os

num_casas_decimais = 2

def create_dataframe(dados):
    return pd.DataFrame(dados).round(num_casas_decimais)

def show_table(df):
    print(df)

def save_table(df, diretorio):
    path = os.path.join(diretorio, "compare_table")
    df.to_csv(path, index=False)

    
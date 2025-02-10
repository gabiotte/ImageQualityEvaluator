import pandas as pd
import os
from collections import defaultdict

num_casas_decimais = 2

def create_dataframe(dados):
    return pd.DataFrame(dados).round(num_casas_decimais)

def show_table(df):
    print(df)

def save_table(df, diretorio):
    path = os.path.join(diretorio, "compare_table")
    df.to_csv(path, index=False)

def max_values(dados):
    max_values = defaultdict(list)
    df = create_dataframe(dados)
    for metric in df.columns:
        if metric == "Imagem":
            continue
        index = df[metric].idxmax()
        max_values[metric].append(dados["Imagem"][index])
        max_values[metric].append(dados[metric][index])
    df_max_values = create_dataframe(max_values)
    return df_max_values



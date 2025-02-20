import pandas as pd
import os
from collections import defaultdict


class Table: 
    def __init__(self, dados):
        self.df = pd.DataFrame(dados).round(2)
        self.dados = dados

    def show(self):
        print(self.df)

    def save(self, diretorio):
        path = os.path.join(diretorio, "metrics_x_images.csv")
        self.df.to_csv(path, index=False)

    def normalized(self):
        normalized = defaultdict(list)
        for metric in self.df.columns:
            if metric == "Imagem":
                continue
            if metric == "Valor de Azul":
                continue
            if metric == "Valor de Verde":
                continue
            if metric == "Valor de Vermelho":
                continue

            max = self.df[metric].max()
            min = self.df[metric].min()

            if metric == "Range RGB":
                for value in self.df[metric]:
                    value = (max - value) / (max - min)
                    normalized[metric].append(value)
                continue


            for value in self.df[metric]:
                value = (value - min) / (max - min)
                normalized[metric].append(value)

        return pd.DataFrame(normalized)    
    

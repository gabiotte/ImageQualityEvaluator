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

    def best_values(self):
        best_values = {}
        for metric in self.df.columns:
            if metric == "Imagem":
                continue
            if metric == "Valor de Azul":
                continue
            if metric == "Valor de Verde":
                continue
            if metric == "Valor de Vermelho":
                continue
            if metric == "Range RGB":
                index = self.df[metric].idxmin()
            else:
                index = self.df[metric].idxmax()

            best_values[metric] = self.df[metric][index]
        return best_values # retorna um dicionário {metric : max_value}
        
    
    def best_image(self):
        best_values = self.best_values()
        best_image = best_values["Imagem"].value_counts().idxmax()
        return best_image

    def diference(self):
        max_values = self.best_values()
        new_table = defaultdict(list)

        for image in self.df["Imagem"]:
            new_table["Imagem"].append(image)
            
        for metric in max_values:
            for value in self.df[metric]:
                value = max_values[metric] - value
                new_table[metric].append(value)

        return pd.DataFrame(new_table)
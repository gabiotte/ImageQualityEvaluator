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
        best_values = defaultdict(list)
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
                
            best_values["Métrica"].append(metric)    
            best_values["Imagem"].append(self.dados["Imagem"][index])
            best_values["Valor"].append(self.dados[metric][index])
            
        df_best_values = pd.DataFrame(best_values)
        return df_best_values
    
    def best_image(self):
        best_values = self.best_values()
        best_image = best_values["Imagem"].value_counts().idxmax()
        return best_image

    
import pandas as pd
import os
from collections import defaultdict
import numpy as np

class Table: 
    def __init__(self, dados):
        self.df = pd.DataFrame(dados).round(2)
        self.df.set_index("Imagem", inplace=True)

    def show(self):
        print(self.df)

    def save(self, diretorio):
        path = os.path.join(diretorio, "metrics_x_images.csv")
        self.df.to_csv(path)

    def normalized(self):
        normalized = defaultdict(list)
        table = self.df.reset_index()

        for metric in table.columns:

            if metric == "Imagem":
                normalized[metric] = table.get(metric)
                continue

            elif metric == "Valor de Azul":
                continue
            elif metric == "Valor de Verde":
                continue
            elif metric == "Valor de Vermelho":
                continue

            max = table[metric].max()
            min = table[metric].min()

            if metric == "Range RGB":
                for value in table[metric]:
                    value = (max - value) / (max - min)
                    normalized[metric].append(value)

                continue

            for value in table[metric]:
                value = (value - min) / (max - min)
                normalized[metric].append(value)
        
        df_normalized = pd.DataFrame(normalized)
        df_normalized.set_index("Imagem", inplace=True)  
        return df_normalized
    
    def std(self):
        images_std = defaultdict(list)
        df_normalized = self.normalized()

        for imagem in df_normalized.index:
            linha = df_normalized.loc[imagem]
            std = np.std(linha)
            images_std["Imagem"].append(imagem)
            images_std["STD"].append(std)
        
        df_images_std = pd.DataFrame(images_std)
        df_images_std.set_index("Imagem", inplace=True)
        return df_images_std
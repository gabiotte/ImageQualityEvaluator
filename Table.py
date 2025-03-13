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

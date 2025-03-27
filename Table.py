import pandas as pd
import os
from collections import defaultdict
import numpy as np
from compare import * 

class Table: 
    def __init__(self, diretorio):
        self.diretorio = diretorio
        self.dados = compare_images(diretorio)
        self.df = pd.DataFrame(self.dados).round(2)
        self.df.set_index("Imagem", inplace=True)

    def show(self):
        print(self.df)

    def save(self):
        path = os.path.join(self.diretorio, "metrics_x_images.csv")
        self.df.to_csv(path)

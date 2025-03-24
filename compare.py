import os
from collections import defaultdict
from Image import *
import pandas as pd

def compare_images(diretorio):
    results = defaultdict(list)

    allowed_ext = (".jpg", ".jpeg", ".bmp")

    for file in os.listdir(diretorio):
        path = os.path.join(diretorio, file)

        if file == "tempo.csv":
            file_path = os.path.join(diretorio,file)
            df_tempo = pd.read_csv(file_path)
            continue

        if not file.lower().endswith(allowed_ext):
            continue

        image = Image(path)

        results["Imagem"].append(file)
        results["Nitidez"].append(image.laplacian_variance())
        results["Desfoque"].append(image.marziliano_blur())
        results["Contraste"].append(image.contrast_rms())
        results["Ruído"].append(image.signal_to_noise_ratio())
            
    return results, df_tempo

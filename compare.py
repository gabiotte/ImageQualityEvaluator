import os
from collections import defaultdict
from Image import *
import pandas as pd

def compare_images(diretorio):
    results = defaultdict(list)

    allowed_ext = (".jpg", ".jpeg", ".bmp")

    capture_time_path = os.path.join(diretorio, "tempo.csv")
    capture_time_df = pd.read_csv(capture_time_path)
    capture_time_df.set_index("Imagem", inplace=True)
    
    for file in os.listdir(diretorio):
        path = os.path.join(diretorio, file)

        if not file.lower().endswith(allowed_ext):
            continue

        image = Image(path)

        results["Imagem"].append(file)
        results["Nitidez"].append(image.laplacian_variance())
        results["Desfoque"].append(image.marziliano_blur())
        results["Contraste"].append(image.contrast_rms())
        results["Ruído"].append(image.signal_to_noise_ratio())
        results["Tempo de Captura (µs)"].append(capture_time_df.loc[file," Tempo (µs)"])
            
    return results
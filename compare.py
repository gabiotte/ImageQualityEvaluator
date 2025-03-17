import os
from collections import defaultdict
from metrics import *
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

        image = load_image(path)

        results["Imagem"].append(file)
        results["Nitidez"].append(laplacian_variance(image))
        results["Desfoque"].append(marziliano_blur(image))
        results["Contraste"].append(contrast_rms(image))
        results["Ruído"].append(signal_to_noise_ratio(image))
            
    return results, df_tempo

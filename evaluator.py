import argparse
import cv2
import numpy as np
import os
from collections import defaultdict
import pandas as pd
from metrics import *

# Função Principal de Avaliação

def compare_images(diretorio):
    results = defaultdict(list)

    for file in os.listdir(diretorio):
        path = os.path.join(diretorio, file)
        image = load_image(path)

        results["Imagem"].append(file)
        results["Nitidez (L)"].append(laplacian_variance(image))
        results["Nitidez (M)"].append(marziliano_blur(image))
        results["Brilho Médio"].append(brightness_mean(image))
        results["Contraste RMS"].append(contrast_rms(image))
        results["Saturação Média"].append(saturation_metrics(image)[0])
        results["DP da Saturação"].append(saturation_metrics(image)[1])
        results["Valor de Azul"].append(color_distribution(image)[0])
        results["Valor de Verde"].append(color_distribution(image)[1])
        results["Valor de Vermelho"].append(color_distribution(image)[2])
        results["SNR"].append(signal_to_noise_ratio(image))
            
    return results

def show_table(dados):
    df = pd.DataFrame(dados).round(2)
    print(df)
    return df

def save_table(df, diretorio):
    path = os.path.join(diretorio, "compare_table")
    df.to_csv(path, index=False)

diretorio = "images"
dados = compare_images(diretorio)
save_table(show_table(dados), diretorio)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Avaliação de Qualidade de Imagem")
#     parser.add_argument("diretorio", type=str, help="Diretório contendo as imagens para análise")

#     args = parser.parse_args()
#     show_table(compare_images(args.diretorio))
import cv2
import numpy as np
import os
from collections import defaultdict
import pandas as pd

def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Erro: a imagem não foi carregada corretamente. Verifique o caminho do arquivo.")
    return image

def convert_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 1. Nitidez

def laplacian_variance(image):
    gray = convert_gray(image)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

def marziliano_blur(image):
    gray = convert_gray(image)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    return np.mean(np.abs(sobelx))

# 2. Exposição

def brightness_mean(image):
    gray = convert_gray(image)
    return np.mean(gray)

def contrast_rms(image):
    gray = convert_gray(image)
    return np.std(gray)

# 3. Cores

def saturation_metrics(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    saturation = hsv[:, :, 1]
    return np.mean(saturation), np.std(saturation)

def color_distribution(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    return np.mean(lab, axis=(0, 1))

# 4. Ruído

def signal_to_noise_ratio(image):
    gray = convert_gray(image)
    mean_signal = np.mean(gray)
    noise = np.std(gray)
    return mean_signal / noise if noise != 0 else 0

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
        results["Distribuição de Cores (BGR)"].append([round(val, 2) for val in color_distribution(image)])
        results["SNR"].append(signal_to_noise_ratio(image))
            
    return results

def show_table(dados):
    df = pd.DataFrame(dados)
    print(df.round(2))

show_table(compare_images("images"))
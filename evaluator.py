import cv2
import numpy as np
from scipy.stats import kurtosis
import matplotlib.pyplot as plt
import os

def load_image(image_path):
    return cv2.imread(image_path)

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

def evaluate_image_quality(image_path):
    image = load_image(image_path)
    
    metrics = {
        "Nitidez (Laplacian)": laplacian_variance(image),
        "Nitidez (Marziliano)": marziliano_blur(image),
        "Brilho Médio": brightness_mean(image),
        "Contraste RMS": contrast_rms(image),
        "Saturação Média": saturation_metrics(image)[0],
        "Desvio Padrão da Saturação": saturation_metrics(image)[1],
        "Distribuição de Cores (LAB)": color_distribution(image),
        "SNR (Signal-to-Noise Ratio)": signal_to_noise_ratio(image)
    }
    
    return metrics

def compare_images(diretorio):
    evaluation = {}
    for file in os.listdir(diretorio):
        path = os.path.join(diretorio, file)
        evaluation[file] = evaluate_image_quality(path)
    
    weights = {
        "Nitidez (Laplacian)": 1.5,
        "Nitidez (Marziliano)": 1.2,
        "Brilho Médio": 1.0,
        "Contraste RMS": 1.3,
        "Saturação Média": 1.1,
        "Desvio Padrão da Saturação": 1.1,
        "SNR (Signal-to-Noise Ratio)": 1.4
    }
    
    scores = {}
    for image in evaluation:
        score = sum(weights[metric] * evaluation[image][metric] for metric in weights)
        scores[image] = score

    best_one = max(scores, key=scores.get)
        
    return scores, best_one

scores, best = compare_images("images")

print(f"\nMelhor imagem:\n  {best}")
print("\nPontuações:")
for filename, score in scores.items():
    print(f"  {filename}: {score:.2f}")
print("\n")
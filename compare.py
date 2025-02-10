import os
from collections import defaultdict
from metrics import *

def compare_images(diretorio):
    results = defaultdict(list)

    allowed_ext = (".jpg", ".jpeg", ".bmp")

    for file in os.listdir(diretorio):
        path = os.path.join(diretorio, file)

        if not file.lower().endswith(allowed_ext):
            continue

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
        results["Range RGB"].append(color_distribution_range(image))
        results["SNR"].append(signal_to_noise_ratio(image))
            
    return results
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
        results["Nitidez"].append(laplacian_variance(image))
        results["Desfoque"].append(marziliano_blur(image))
        results["Contraste"].append(contrast_rms(image))
        results["Ruído"].append(signal_to_noise_ratio(image))
            
    return results
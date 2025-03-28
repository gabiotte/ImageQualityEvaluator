import cv2
import numpy as np

def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Erro: a imagem {image_path} não foi carregada corretamente. Verifique o caminho do arquivo.")
    return image

def convert_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

class Image:
    def __init__(self, image_path):
        self.image = load_image(image_path)
        self.capture_time = 0
    
    def set_capture_time(self,time):
        self.capture_time = time

    # 1. Nitidez

    def laplacian_variance(self):
        gray = convert_gray(self.image)
        return cv2.Laplacian(gray, cv2.CV_64F).var()

    # 2. Ausência de desfoque

    def marziliano_blur(self):
        gray = convert_gray(self.image)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        return np.mean(np.abs(sobelx))

    # 3. Contraste

    def contrast_rms(self):
        gray = convert_gray(self.image)
        return np.std(gray)

    # 4. Ruído

    def signal_to_noise_ratio(self):
        gray = convert_gray(self.image)
        mean_signal = np.mean(gray)
        noise = np.std(gray)
        return mean_signal / noise if noise != 0 else 0
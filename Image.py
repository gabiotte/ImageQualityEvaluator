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
    def __init__(self, image_path, x, y, w, h):
        self.image = load_image(image_path)
        self.capture_time = 0
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def set_capture_time(self,time):
        self.capture_time = time

# 1. Ruído
    def noise(self):
        gray = convert_gray(self.image)
        
        patch = gray[self.y:self.y + self.h, self.x:self.x + self.w]
        
        return np.std(patch)

# 2. Desfoque
    def blur(self):
        gray = convert_gray(self.image)
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        return laplacian.var()
    
# 3. Contraste
    def contrast(self):
        gray = convert_gray(self.image)
        return np.std(gray)
    
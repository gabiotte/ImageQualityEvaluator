import argparse
from compare import *
from Table import *

cameras = ["gc0308", "nt99141", "ov2640", "ov7670"]
for camera in cameras:
    print("\n\n----------------------- ", camera, " ----------------------- \n")

    for group in os.listdir(camera):
        path = os.path.join(camera, group)
        
        # Faz a comparação e cria o dataframe
        dados = compare_images(path)
        df = Table(dados)
        
        df.save(path)
        print(f"\n\nTabela Metricas x Imagens {group} salva\n")
        df.show()
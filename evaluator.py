import argparse
from compare import *
from Table import *

main_dir = "projeto"

for camera in os.listdir(main_dir):

    print("\n\n----------------------- ", camera, " ----------------------- \n")

    camera_path = os.path.join(main_dir, camera)
    for group in os.listdir(camera_path):
        path = os.path.join(camera_path, group)
        
        # Faz a comparação e cria o dataframe
        df = Table(path)
        
        df.save()
        print(f"\n\nTabela Metricas x Imagens {group} salva\n")
        df.show()
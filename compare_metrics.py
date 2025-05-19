import os
import pandas as pd
from collections import defaultdict
from calculate_metrics import save

def compare_cameras(diretorio):

    linhas = []

    # Abre a pasta de cada câmera 
    for camera in os.listdir(diretorio):
        camera_path = os.path.join(diretorio,camera)
        if os.path.isdir(camera_path):

            # Abre o arquivo comparação.xlsx e tranforma em um DF
            comparacao_path = os.path.join(camera_path,"comparacao.xlsx")
            camera_df = pd.read_excel(comparacao_path)  
            print(camera_df)

            # Calcula as médias, menos da primeira coluna (Imagem) e da útima (Tempo de captura)
            metrics = camera_df.iloc[:, 1:-1].mean()

            # Calcula a moda da útima coluna (Tempo de Captura)
            last_column = (camera_df.columns)[-1]
            capture_time = camera_df[last_column].mode().iloc[0]

            # Adiciona tudo ao dicionário
            linhas.append({"Camera":camera, **metrics.to_dict(), last_column: capture_time})
            
    # Tranforma o dicionário em DF
    final_df = pd.DataFrame(linhas)

    # Salva o DF como um arquivo xlsx
    save(diretorio, final_df)
import os
from collections import defaultdict
from Image import *
import pandas as pd

def compare_group_images(group_path, group):
    results = defaultdict(list)

    allowed_ext = (".jpg", ".jpeg", ".bmp")

    capture_time_path = os.path.join(group_path, "tempo.csv")
    capture_time_df = pd.read_csv(capture_time_path)
    capture_time_df.set_index("Imagem", inplace=True)
    
    for file in os.listdir(group_path):
        path = os.path.join(group_path, file)

        if not file.lower().endswith(allowed_ext):
            continue

        image = Image(path)

        results["Grupo"].append(group)
        results["Imagem"].append(file)
        results["Nitidez"].append(image.laplacian_variance())
        results["Desfoque"].append(image.marziliano_blur())
        results["Contraste"].append(image.contrast_rms())
        results["Ruído"].append(image.signal_to_noise_ratio())
        results["Tempo de Captura (µs)"].append(capture_time_df.loc[file," Tempo (µs)"])
            
    results_df = pd.DataFrame(results).round(2)
    return results_df

def camera_table(camera_path):
    table_df = pd.DataFrame()

    for group in os.listdir(camera_path):
        
        group_path = os.path.join(camera_path, group)
        if not os.path.isdir(group_path):
            continue

        group_results_df = compare_group_images(group_path, group)

        table_df = pd.concat([group_results_df, table_df])
    
    table_path = os.path.join(camera_path,"comparacao.csv")
    save(table_df,table_path)

    return table_df

def save(dataframe, path):
    dataframe.to_csv(path)
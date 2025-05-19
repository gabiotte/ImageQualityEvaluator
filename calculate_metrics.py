import os
from collections import defaultdict
from Image import *
import pandas as pd

def create_compare_table(dir):
    results = defaultdict(list)

    allowed_ext = (".jpg", ".jpeg", ".bmp")

    # Abre os arquivos csv
    selecoes_path = os.path.join(dir, "selecoes.csv")
    capture_time_path = os.path.join(dir, "tempo.csv")

    # Cria o DF do tempo de captura
    if os.path.exists(capture_time_path):
        capture_time_df = pd.read_csv(capture_time_path)
        capture_time_df.set_index("Imagem", inplace=True)
    
    # Cria o DF das coordenadas do ruído
    selecoes_df = pd.read_csv(selecoes_path)
    selecoes_df.set_index("Imagem", inplace=True)

    # Abre todos os arquivos de imagem
    for file in os.listdir(dir):
        path = os.path.join(dir, file)

        if not file.lower().endswith(allowed_ext):
            continue
        
        # Pega as coordenadas do ruído
        linha = selecoes_df.loc[file]
        x, y, w, h = int(linha["x"]), int(linha["y"]), int(linha["w"]), int(linha["h"])
        
        # Instancia o objeto imagem
        image = Image(path, x, y, w, h)

        # Adiciona os resultados em um DF
        results["Imagem"].append(file)
        results["Nitidez"].append(image.blur())
        results["Contraste"].append(image.contrast())
        results["Ruído"].append(image.noise())
        if os.path.exists(capture_time_path):
            results["Tempo de Captura (µs)"].append(capture_time_df.loc[file," Tempo (µs)"])
    
    # Arredonda os valores e retorna o DF
    results_df = pd.DataFrame(results).round(2)
    return results_df

def save(dir, dataframe):
    path = os.path.join(dir,"comparacao.xlsx")

    # Salva o DF em um arquivo excel
    with pd.ExcelWriter(path) as writer:
        dataframe.to_excel(writer, index=False)

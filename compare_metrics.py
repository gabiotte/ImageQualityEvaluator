import os
import pandas as pd
from collections import defaultdict
from calculate_metrics import calculate_metrics, save

def compare_cameras(diretorio):

    linhas = []

    # Abre a pasta de cada câmera 
    for camera in os.listdir(diretorio):
        camera_path = os.path.join(diretorio,camera)
        if os.path.isdir(camera_path):

            # Abre o arquivo comparação.xlsx e tranforma em um DF
            comparacao_path = os.path.join(camera_path,"comparacao.xlsx")

            if not os.path.exists(comparacao_path):
                print(f"[!] Arquivo não encontrado em {camera_path}. Calculando métricas e gerando o arquivo.")
                calculate_metrics(camera_path)

            camera_df = pd.read_excel(comparacao_path)  

            # Calcula as médias, menos da primeira coluna (Imagem) e da útima (Tempo de captura)
            metrics = camera_df.iloc[:, 1:-1].mean()

            # Calcula a média arredondada da útima coluna (Tempo de Captura)
            last_column = (camera_df.columns)[-1]
            capture_time = camera_df[last_column].mean().round(0)

            # Abre o aquivo tempo.csv e transforma em um DF
            time_path = os.path.join(camera_path, "tempo.csv")
            time_df = pd.read_csv(time_path)
            time_df.set_index("Imagem", inplace=True)
             
            # Encontra o tempo de inicialização
            init_time = time_df.loc["camera","Tempo (µs)"]

            # Adiciona tudo ao dicionário
            linhas.append({"Camera":camera, **metrics.to_dict(), last_column: capture_time, "Inicialização (µs)":init_time})
            
    # Tranforma o dicionário em DF
    final_df = pd.DataFrame(linhas)

    # Salva o DF como um arquivo xlsx
    save(diretorio, final_df)

def gerar_medias_agrupadas(diretorio):

    # Abre o arquivo de comparação
    caminho = os.path.join(diretorio, "comparacao.xlsx")
    if not os.path.exists(caminho):
        print(f"Arquivo comparacao.xlsx não encontrado em {diretorio}")
        return

    df = pd.read_excel(caminho)

    if "Camera" not in df.columns:
        print(f"Coluna 'Camera' não encontrada em {caminho}")
        return

    # Extrai o nome do sensor antes do .
    df["Grupo"] = df["Camera"].astype(str).apply(lambda x: x.split(".")[0])

    # Converte todas as colunas de métricas para numérico e exclui as de camera e grupo
    metricas = df.drop(columns=["Camera", "Grupo"], errors="ignore")
    metricas = metricas.apply(pd.to_numeric, errors="coerce")

    # Junta o grupo de volta 
    df_grupos = pd.concat([df[["Grupo"]], metricas], axis=1)

    # Agrupa as cameras e calcula a média
    df_medias = df_grupos.groupby("Grupo").mean(numeric_only=True).round(2).reset_index()
    df_medias.rename(columns={"Grupo": "Camera"}, inplace=True)

    # Salva o resultado final
    saida = os.path.join(diretorio, "resultado.xlsx")
    df_medias.to_excel(saida, index=False)
    print(f"Resultado salvo em: {saida}")
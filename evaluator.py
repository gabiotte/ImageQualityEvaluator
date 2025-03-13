import argparse
from compare import *
from Table import *

diretorios = ["GC 0308", "NT 99141", "OV 2640", "OV 7670"]
for diretorio in diretorios:
    print("\n\n----------------------- ", diretorio, " ----------------------- \n")

    # Faz a comparação e cria o dataframe
    dados = compare_images(diretorio)
    df = Table(dados)
    
    df.save(diretorio)
    print("Tabela Metricas x Imagens salva\n")
    df.show()
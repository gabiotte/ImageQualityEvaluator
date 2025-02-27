import argparse
from compare import *
from Table import *
from relatorio import *

diretorios = ["GC 0308", "NT 99141", "OV 2640", "OV 7670"]
for diretorio in diretorios:
    print("\n\n----------------------- ", diretorio, " ----------------------- \n")

    # Faz a comparação e cria o dataframe
    dados = compare_images(diretorio)
    df = Table(dados)
    
    # std_sorted = df.std_sorted()
    # avg_sorted = df.avg_sorted()
    # print(avg_sorted,"\n\n",std_sorted)

    # print(df.normalized())

    # Mostrar tabela de comparação
    print("Tabela Metricas x Imagens:")
    df.show()

    # Mostrar melhores valores para cada métrica
    # print("\nMelhores Valores para Cada Métrica:\n",df.best_values())

    # # Salva a tabela e o relatório
    # df.save(diretorio)
    # gerar_relatório(dados, diretorio)



# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Avaliação de Qualidade de Imagem")
#     parser.add_argument("diretorio", type=str, help="Diretório contendo as imagens para análise")

#     args = parser.parse_args()
#     show_table(compare_images(args.diretorio))
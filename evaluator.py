import argparse
from compare import *
from DataHandler import *

diretorio = "images"
dados = compare_images(diretorio)
df = DataHandler(dados)

df.show()
# max = df.best_values()
# max.show()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Avaliação de Qualidade de Imagem")
#     parser.add_argument("diretorio", type=str, help="Diretório contendo as imagens para análise")

#     args = parser.parse_args()
#     show_table(compare_images(args.diretorio))
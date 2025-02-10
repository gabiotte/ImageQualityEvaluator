import argparse
from compare import *
from data import *

diretorio = "images"
dados = compare_images(diretorio)
df = create_dataframe(dados)
show_table(df)
save_table(df, diretorio)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Avaliação de Qualidade de Imagem")
#     parser.add_argument("diretorio", type=str, help="Diretório contendo as imagens para análise")

#     args = parser.parse_args()
#     show_table(compare_images(args.diretorio))
import argparse
from compare import *
from DataFrame import *

diretorio = "images"
dados = compare_images(diretorio)
df = DataFrame(dados)

print("Tabela Metricas x Imagens:")
df.show()
print("\nMelhores Valores para Cada Métrica:\n",df.best_values())
print("\nImagem com Melhores Resultados: ", df.best_image())

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Avaliação de Qualidade de Imagem")
#     parser.add_argument("diretorio", type=str, help="Diretório contendo as imagens para análise")

#     args = parser.parse_args()
#     show_table(compare_images(args.diretorio))
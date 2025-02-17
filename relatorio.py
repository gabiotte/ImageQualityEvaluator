from Table import *

def gerar_relatório(dados): 
    table = Table(dados)
    file = open("relatorio.txt", "w")

    file.write("Imagem com os melhores resultados: ", table.best_image())
    
    
    
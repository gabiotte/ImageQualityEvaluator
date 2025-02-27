from Table import *
import pandas

def gerar_relatório(dados, diretorio): 
    table = Table(dados)
    file = open(diretorio + "/relatorio.txt", "w")

    file.write("Imagem com os melhores resultados: " + table.best_image() + "\n\n")

    best_v = table.best_values()
    for metric in best_v:
        value = best_v[metric][1].round(2)
        linha = f"{metric}: {best_v[metric][0]} ({value})\n"
        file.write(linha)
            
    
     
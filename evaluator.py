import argparse
from calculate_metrics import *
from compare_metrics import *

def main(main_dir, modo):
    if not os.path.isdir(main_dir):
        print(f"[✘] Diretório inválido: {main_dir}")
        return
    
    if modo in ["calcular"]:
        print("Calculando métricas...")
        print(calculate_metrics(main_dir))        

    if modo in ["comparar"]:
        print("Comparando métricas...")
        compare_cameras(main_dir)

    if modo in ["media"]:
        print("Calculando médias agrupadas por câmera...")
        gerar_medias_agrupadas(main_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calcula as métricas das fotos ou compara as métricas de cada câmera"
    )
    parser.add_argument("--diretorio", type=str, required=True, 
                        help="Diretório onde estão as fotos ou as câmeras")
    parser.add_argument("--modo", type=str, choices=["calcular", "comparar", "media"],
                        help="Modo de execução: 'calcular', 'comparar' ou 'media'")

    args = parser.parse_args()
    main(args.diretorio, args.modo)
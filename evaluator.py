import argparse
from compare import *

def main(main_dir):
    if not os.path.isdir(main_dir):
        print(f"[✘] Diretório inválido: {main_dir}")
        return
    
    compare_table = create_compare_table(main_dir)
    print(compare_table)
    save(main_dir, compare_table)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Gera uma tabela comparativa para cada câmera em um diretório."
    )
    parser.add_argument("--diretorio", type=str, required=True, help="Diretório principal onde estão as fotos"
    )

    args = parser.parse_args()
    main(args.diretorio)
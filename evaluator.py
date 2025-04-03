import argparse
from compare import *

def main(main_dir):
    if not os.path.isdir(main_dir):
        print(f"[✘] Diretório inválido: {main_dir}")
        return
    
    for camera in os.listdir(main_dir):
        if camera.startswith("."):
            continue

        camera_path = os.path.join(main_dir, camera)

        if os.path.isdir(camera_path):
            print("\n\n----------------------- ", camera, " ----------------------- \n")
            print(camera_table(camera_path))
        else:
            print(f"[!] Ignorado (não é diretório): {camera_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Gera uma tabela comparativa para cada câmera em um diretório."
    )
    parser.add_argument("--diretorio", type=str, required=True, help="Diretório principal onde estão as pastas das câmeras"
    )

    args = parser.parse_args()
    main(args.diretorio)
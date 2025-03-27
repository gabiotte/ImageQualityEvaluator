import argparse
from compare import *

parser = argparse.ArgumentParser()
parser.add_argument("--diretorio", type=str, required=True, help="Diretório principal do projeto")
args = parser.parse_args()

main_dir = args.diretorio

for camera in os.listdir(main_dir):

    print("\n\n----------------------- ", camera, " ----------------------- \n")

    camera_path = os.path.join(main_dir, camera)
    print(camera_table(camera_path))
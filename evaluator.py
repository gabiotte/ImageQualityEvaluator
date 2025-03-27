import argparse
from compare import *
from Table import *

main_dir = "projeto"

for camera in os.listdir(main_dir):

    print("\n\n----------------------- ", camera, " ----------------------- \n")

    camera_path = os.path.join(main_dir, camera)
    print(create_table(camera_path))
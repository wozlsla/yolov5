import os
import shutil

from natsort import natsorted

# Specify the paths for your images and labels directories
name = "exp"

src_directory = f"/home/dataset/2024_get_data/{name}/"
dest_directory = f"/home/dataset/2024_get_data/{name}/steps/"


def move_data_every_n_steps(src_path, dest_path, n=0):
    image_files = natsorted([f for f in os.listdir(os.path.join(src_path, 'images')) if f.endswith('.jpg')])
    label_files = natsorted([f for f in os.listdir(os.path.join(src_path, 'bbox_labels')) if f.endswith('.txt')])

    os.makedirs(os.path.join(src_path, 'steps'), exist_ok=False)
    os.makedirs(os.path.join(dest_path, 'bbox_labels'), exist_ok=False)

    for i in range(0, len(image_files), n):
        image_file = image_files[i]
        label_file = label_files[i]

        src_image_path = os.path.join(src_path, 'images', image_file)
        src_label_path = os.path.join(src_path, 'bbox_labels', label_file)

        dest_image_path = os.path.join(dest_path, image_file)
        dest_label_path = os.path.join(dest_path, 'bbox_labels', label_file)

        shutil.copy(src_image_path, dest_image_path)
        shutil.copy(src_label_path, dest_label_path)
        
move_data_every_n_steps(src_directory, dest_directory, n=3)
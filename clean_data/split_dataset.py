import os
import random
import shutil


path = "/home/dataset/v1/train"
path_2 = "/home/dataset/v2/train"


# Make dirs
src_images_dir = f"{path}/images"
src_labels_dir = f"{path}/labels"

dst_images_dir = f"{path}/images_split"
dst_labels_dir = f"{path}/labels_split"
# dst_images_dir = f"{path_2}/images"
# dst_labels_dir = f"{path_2}/labels"

os.makedirs(dst_images_dir, exist_ok=True)
os.makedirs(dst_labels_dir, exist_ok=True)


# Get file names
img_dir = os.path.join(path, "images")
# img_files = sorted(os.listdir(img_dir))[:4000]
# img_files = sorted(os.listdir(img_dir))[4000:4830] # 829
img_files = random.sample(os.listdir(img_dir), 20)


# Move/Copy
for img_file in img_files:
    file_name = os.path.splitext(img_file)[0]
    label_file_name = f"{file_name}.txt"

    src_image_path = os.path.join(src_images_dir, img_file)
    src_label_path = os.path.join(src_labels_dir, label_file_name)

    dst_image_path = os.path.join(dst_images_dir, img_file)
    dst_label_path = os.path.join(dst_labels_dir, label_file_name)

    # shutil.move(src_image_path, dst_image_path)
    # shutil.move(src_label_path, dst_label_path)
    shutil.copyfile(src_image_path, dst_image_path)
    shutil.copyfile(src_label_path, dst_label_path)


print(f"{len(img_files)} files moved to {dst_images_dir} and {dst_labels_dir}.")
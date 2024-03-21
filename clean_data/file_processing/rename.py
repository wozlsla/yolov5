import os
import subprocess

# dataset = "train"
# dataset = "valid"
dataset = "test"

name = f"ppe_v1_{dataset}"
dataset_path = f"/home/dataset/v1/{dataset}/"


def get_cnt(path):
    command_1 = f"find {path}/images -type f -name '*.jpg' | wc -l"
    command_2 = f"find {path}/labels -type f -name '*.txt' | wc -l"
    output_1 = subprocess.check_output(command_1, shell=True).decode("utf-8").strip()
    output_2 = subprocess.check_output(command_2, shell=True).decode("utf-8").strip()
    print(f"Images: {output_1}, Labels: {output_2}")

    if output_1 == output_2:
        rename(path, name)
    return


def rename(path, name):
    img_dir = os.path.join(path, "images")
    lab_dir = os.path.join(path, "labels")

    img_files = sorted(os.listdir(img_dir))
    lab_files = sorted(os.listdir(lab_dir))

    for idx, (img_file, lab_file) in enumerate(zip(img_files, lab_files)):
        img_src = os.path.join(img_dir, img_file)
        lab_src = os.path.join(lab_dir, lab_file)
        img_dst = os.path.join(img_dir, f"{name}_{idx}.jpg")
        lab_dst = os.path.join(lab_dir, f"{name}_{idx}.txt")

        os.rename(img_src, img_dst)
        os.rename(lab_src, lab_dst)
    print(f"Dataset: {dataset}")
    print(f"Total: {idx + 1}")
    return


get_cnt(dataset_path)


# items_2 = sorted(glob.glob(f"{path}/labels/*.txt"))
# items_1 = sorted(glob.glob(f"{path}/images/*.jpg"))

# items_1 = sorted(os.listdir(os.path.join(path, "images")))
# items_1 = sorted(os.listdir(f"{path}images"))
# imgs = sorted(os.listdir(path + "images"))
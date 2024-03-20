import os

name = "exp"
dataset = "valid"

path = f"/home/dataset/{dataset}/{name}/labels"
files = os.listdir(path)


for filename in files:
    if filename.startswith("stream2"):
        new_name = filename.replace("stream2", f"{name}")

        old_path = os.path.join(path, filename)
        new_path = os.path.join(path, new_name)
        os.rename(old_path, new_path)

        print(old_path.split("/")[-1], new_path.split("/")[-1])
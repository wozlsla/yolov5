import os


def merge_files_with_same_name(dir1, dir2):
    files_dir1 = os.listdir(dir1)
    files_dir2 = os.listdir(dir2)

    common_files = list(set(files_dir1) & set(files_dir2))

    for file in common_files:
        with open(os.path.join(dir1, file), "r") as file1, open(os.path.join(dir2, file), "r") as file2:
            content1 = file1.readlines()
            content2 = file2.readlines()

            merged_content = content1 + [line for line in content2 if line not in content1]

            with open(os.path.join(dir1, file), "w") as merged_file:
                merged_file.write("".join(merged_content))


# Replace dir paths with the actual paths to perform the merge
dir1_path = "/home/dataset/train/labels/"
dir2_path = "/home/dataset/train/labels_person/"

merge_files_with_same_name(dir1_path, dir2_path)
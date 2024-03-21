import os
import glob


class Convertor:
    def __init__(self):
        pass

    def convert_cls(self, f_path, lines, cls_num, to_num=0):
        for idx, line in enumerate(lines):
            parts = line.split()  # get cls num
            if parts[0] == str(cls_num):  # 첫 line 공백 처리 필요
                parts[0] = str(to_num)
                n_line = " ".join(parts) + "\n"
                lines[idx] = n_line

            with open(f_path, "w") as f:
                for i in lines:
                    f.write(i)

    def remove_cls(self, f_path, lines, rm_num):
        with open(f_path, "w") as f:
            for line in lines:
                # if line.startswith(rm_num + " "): # TypeError: can only concatenate list (not "str") to list
                if not line.startswith(f"0 "):
                    # if not line.startswith(f"10 "):
                    f.write(line)
                # if int(line[0]) not in rm_num:
                #     f.write(line)


def convert(dir_path, func=None, rm_num=None, cls_num=None, to_num=None):
    for f_name in os.listdir(dir_path):
        if f_name.endswith(".txt"):  # label
            f_path = os.path.join(dir_path, f_name) 

            with open(f_path, "r") as f:
                lines = f.readlines()  # get lines
                print(f_name)
                print(lines)
                if func == "remove":
                    remove = Convertor().remove_cls(f_path, lines, rm_num)
                if func == "convert":
                    convert = Convertor().convert_cls(f_path, lines, cls_num, to_num)
                print(lines)
                print()
    return


dataset = ["train", "test", "valid"]
ver = "v7"

# rm_num = [4, 5, 6, 7, 8, 9, 10]

cls_num = 0  # default
to_num = 4  # person

for dir_name in dataset:
    dir_path = f"/home/dataset/{ver}/{dir_name}/labels/"
    # convert(dir_path, func="remove", rm_num=rm_num)
    convert(dir_path, func="convert", cls_num=cls_num, to_num=to_num)


'''
# convert cls num
for f_name in os.listdir(dir_path):
    if f_name.endswith(".txt"):
        input_file = os.path.join(dir_path, f_name)
        with open(input_file, "r") as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                parts = line.split() # get cls num
                if parts[0] == "7" or parts[0] == "8":
                    parts[0] = "0" # convert
                    new_line = " ".join(parts) + "\n"
                    lines[idx] = new_line

        with open(input_file, "w") as f:
            for i in lines:
                f.write(i)


# rm cls num
for f_name in os.listdir(dir_path):
    if f_name.endswith(".txt"):
        f_path = os.path.join(dir_path, f_name)
        with open(f_path, "r") as f:
            lines = f.readlines()

        with open(f_path, "w") as f:
            for line in lines:
                if line.startswith("5 "):
                    f.write(line)


# glob
for file in glob.glob(f'{dir_path}*.txt'):
    # with open(file, 'r') as input_file, open(file, 'w') as output_file:
    with open(file, 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            parts = line.split()
            parts[0] = '3'
            new_line = ' '.join(parts) + '\n' # Write the modified line to the output file
            output_file.write(new_line)
'''
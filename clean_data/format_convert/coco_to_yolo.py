import os
import json
import glob


# 원본 annotation 파일들이 있는 경로
ann_dir = "/home/dataset/songdo/labels_json/"
ann_list = glob.glob(os.path.join(ann_dir, "*.json"))
print(f"Length: {len(ann_list)}")

# Image resolution for all files
img_width, img_height = 1920, 1080

# Class mapping for YOLOv5 format
class_mapping = {
    "01": 0,  # 1. belt
    "05": 1,  # 5. boots
    "07": 2,  # 7. hardhat
}


def convert_to_yolo(json_data, class_mapping, img_width, img_height):
    data = json_data
    img = data["image"]
    print_buffer = []

    for annotation in data["annotations"]:
        try:  # bbox
            class_label = annotation["class"]
            class_index = class_mapping.get(class_label, -1)  # -1: default
            if class_index == -1:
                raise ValueError(f"Class label '{class_label}' not found in the class mapping.")

            xmin, ymin, xmax, ymax = annotation["box"]
            x_center = (xmin + xmax) / 2
            y_center = (ymin + ymax) / 2
            width = xmax - xmin
            height = ymax - ymin

            # Normalize coordinates
            x_center /= img_width
            y_center /= img_height
            width /= img_width
            height /= img_height

            yolo_format = f"{class_index} {x_center:.3f} {y_center:.3f} {width:.3f} {height:.3f}"
            print_buffer.append(yolo_format)

        except:  # polygon
            pass

    # Save
    save_file_name = os.path.join("labels", img["filename"].replace(".jpg", ".txt"))
    print("\n".join(print_buffer), file=open(save_file_name, "w"))


cnt = 0
for anno in ann_list:
    # Load JSON data
    with open(anno, encoding="utf-8-sig", errors="ignore") as json_file:
        json_data = json.load(json_file)

    # Convert to YOLOv5 format
    convert_to_yolo(json_data, class_mapping, img_width, img_height)
    cnt += 1

print(f"Done {cnt}")

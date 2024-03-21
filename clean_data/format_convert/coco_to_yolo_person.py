# -*- coding: utf-8 -*-

"""coco2kitti.py: Converts MS COCO annotation files to
                  Kitti format bounding box label files
__author__ = "haram roh"
"""

import os
from pycocotools.coco import COCO


def coco2yolo(catNms, annFile):
    # initialize COCO api for instance annotations
    coco = COCO(annFile)

    # Create an index for the category names
    cats = coco.loadCats(coco.getCatIds())  # 80
    cat_idx = {}
    for c in cats:
        # {1: 'person', 2: 'bicycle', ...}
        cat_idx[c["id"]] = c["name"]

    for img in coco.imgs:
        # Get all annotation IDs for the image
        catIds = coco.getCatIds(catNms=catNms)
        annIds = coco.getAnnIds(
            imgIds=[img], catIds=catIds
        )  # Image id, Category id를 input으로, 그에 해당하는 annotation id를 return 하는 함수

        # If there are annotations, create a label file
        if len(annIds) > 0:
            img_fname = coco.imgs[img]["file_name"]  # Get image filename
            img_height = coco.imgs[img]["height"]
            img_width = coco.imgs[img]["width"]

            with open("./labels/" + img_fname.split(".")[0] + ".txt", "w") as label_file:
                anns = coco.loadAnns(annIds)

                print_buffer = []

                for a in anns:
                    if a["bbox"]:  # "bbox" : [x,y,width,height]
                        # xmin, ymin, xmax, ymax = a["bbox"]
                        x, y, w, h = a["bbox"]  # coco dataset
                        x_center = (x + w / 2) / img_width
                        y_center = (y + h / 2) / img_height
                        width = w / img_width
                        height = h / img_height

                        # catname = cat_idx[int(a["category_id"])]
                        class_index = a["category_id"]

                        # Format line in label file
                        yolo_format = f"{class_index} {x_center:.3f} {y_center:.3f} {width:.3f} {height:.3f}"
                        print_buffer.append(yolo_format)

                label_file.write("\n".join(print_buffer))


if __name__ == "__main__":
    dataDir = "/home/dataset/coco/train/to_yolo"
    # dataType = "instances_val2017"
    dataType = "instances_train2017"
    annFile = "%s/%s.json" % (dataDir, dataType)
    catNms = ["person"]

    if os.path.isdir("./labels"):
        print("Labels folder already exists - exiting to prevent badness")
    else:
        os.mkdir("./labels")
        coco2yolo(catNms, annFile)

'''
(base) [tmp]$ python pair_check_mask.py 
Labels without images:
2479_CRS_36_03.txt
Total images: 306
Total labels: 307
(base) [tmp]$ python pair_check_mask.py 
Total images: 306
Total labels: 306
'''

import os

images_dir = '/home/dataset/ai_hub/mask/images/'
labels_dir = '/home/dataset/ai_hub/mask/labels/'

image_files = {os.path.splitext(file)[0] for file in os.listdir(images_dir)}
label_files = {os.path.splitext(file)[0] for file in os.listdir(labels_dir)}


# Find image files without a corresponding label file
unmatched_images = image_files - label_files

if unmatched_images:
    print("Images without labels:")
    for image in unmatched_images:
        print(f"{image}.jpg or {image}.JPG")


# Find label files without a corresponding image file
unmatched_labels = label_files - image_files

if unmatched_labels:
    print("Labels without images:")
    for label in unmatched_labels:
        print(f"{label}.txt")


print(f"Total images: {len(image_files)}")
print(f"Total labels: {len(label_files)}")
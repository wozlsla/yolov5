import os

name = "exp"

directory = f"/home/dataset/train/exp/{name}"
images = os.listdir(os.path.join(directory, 'images'))


for i, img_name in enumerate(images):

    index = int(img_name.split('_')[1].split('.')[0])
    new_img_name = f"{name}_{index}.jpg"

    old_img_path = os.path.join(directory, 'images', img_name)
    new_img_path = os.path.join(directory, 'images', new_img_name)

    os.rename(old_img_path, new_img_path)
    
print("Files renamed successfully.")
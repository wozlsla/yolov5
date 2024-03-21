# coding:utf-8
import os
import json
import pandas as pd
from collections import OrderedDict

# (파일명)중복을 제거하고 남은 이미지에서 다시 한번 클래스의 분포를 확인
# annoResampleDir = "/home2/scatterx/dataset_ppe/v5/train/songdo/labels/"
# annoResampleDir = "/home2/scatterx/dataset_ppe/v5/train/hanam/labels/"
annoResampleDir = "/home/dataset/train/5class_resampling_labels/"


annoResampleList = os.listdir(annoResampleDir)
print(len(annoResampleList))
print(annoResampleList[:4])

anno_dict_resample = {"01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0, "09": 0, "10": 0}


# json
for anno in annoResampleList:
    with open(annoResampleDir + anno, encoding="utf-8-sig", errors="ignore") as json_file:
        jsonData = json.load(json_file)
    imgPath = anno.replace(".json", ".jpg")
    df = pd.json_normalize(jsonData)
    filename = df["image.filename"][0]
    # print(df["image.filename"][0])
    for i in range(len(df["annotations"][0])):
        item = df["annotations"][0][i]["class"]
        anno_dict_resample[item] += 1
        # if int(item) < 8:
        #     anno_dict_resample[item] += 1


ordered_dict = OrderedDict(sorted(anno_dict_resample.items(), key=lambda t: t[1], reverse=True))
print(ordered_dict)
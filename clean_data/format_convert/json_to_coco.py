# coding:utf-8

import os
import json

# 코드를 실행하기 전에 이미지-json 파일이 정확한 쌍을 이루는지 먼저 확인해주세요.

# 원본 annotation 파일들이 있는 경로
annoDir = "/home/dataset/songdo/labels/"

# image가 있는 경로
imageDir = "/home/dataset/songdo/images/"

# anno_dir 내 annotation 파일 이름 리스트업
annoList = os.listdir(annoDir)
print(len(annoList))

# cocoDict에 필요한 images, annotations 정보들의 리스트
imgTmpDict = []
annoTmpDict = []

idNum = 1
annoIdNum = 60000
for anno in annoList:
    with open(annoDir + anno, encoding="utf-8-sig", errors="ignore") as json_file:
        jsonData = json.load(json_file)

    imgPath = anno.replace(".json", ".jpg")
    imgSize = 1920 * 1080

    try:
        images = {
            "license": 1,
            "file_name": jsonData["image"]["filename"],
            "coco_url": "",
            "height": jsonData["image"]["resolution"][1],
            "width": jsonData["image"]["resolution"][0],
            "date_captured": jsonData["image"]["date"],
            "flickr_url": "",
            "id": idNum,
        }
    except:
        images = {
            "license": 1,
            "file_name": jsonData["image"]["filename"],
            "coco_url": "",
            "width": 1920,
            "height": 1080,
            "date_captured": jsonData["image"]["date"],
            "flickr_url": "",
            "id": idNum,
        }
    imgTmpDict.append(images)

    for i in range(len(jsonData["annotations"])):
        try:  # bbox 정보가 존재할 경우
            bbox = [
                jsonData["annotations"][i]["box"][0],
                jsonData["annotations"][i]["box"][1],
                jsonData["annotations"][i]["box"][2] - jsonData["annotations"][i]["box"][0],
                jsonData["annotations"][i]["box"][3] - jsonData["annotations"][i]["box"][1],
            ]
            annotation = {
                "segmentation": [],
                "area": "",
                "iscrowd": "",
                "image_id": idNum,
                "bbox": bbox,
                "category_id": int(jsonData["annotations"][i]["class"]),
                "id": annoIdNum,
                "flags": jsonData["annotations"][i]["flags"],
            }
        except:  # polygon 정보가 존재할 경우
            annotation = {
                "segmentation": jsonData["annotations"][i]["polygon"],
                "area": "",
                "iscrowd": "",
                "image_id": idNum,
                "bbox": [0, 0, 0, 0],
                "category_id": int(jsonData["annotations"][i]["class"]),
                "id": annoIdNum,
                "flags": jsonData["annotations"][i]["flags"],
            }
        annoTmpDict.append(annotation)
        annoIdNum += 1
    idNum += 1

# COCO format annotation이 저장될 dict
cocoDict = {}

cocoDict["info"] = {
    "description": "AI Hub 공사현장 안정장비 인식 데이터셋",
    "url": "https://aihub.or.kr/aidata/33921",
    "version": "1.0",
    "year": 2021,
    "contributor": "Haram roh",
    "date_created": "2021/07/22",
}

cocoDict["licenses"] = [{"url": "https://aihub.or.kr/aidata/33921", "id": 1, "name": "미디어그룹사람과숲(컨)"}]

cocoDict["images"] = imgTmpDict
cocoDict["annotations"] = annoTmpDict

cocoDict["categories"] = [
    {"supercategory": "S2", "id": 1, "name": "안전벨트 착용"},
    {"supercategory": "S2", "id": 5, "name": "안전화 착용"},
    {"supercategory": "S2", "id": 7, "name": "안전모 착용"},
]

with open("/home/dataset/3class_coco.json", "w") as f:
    json.dump(cocoDict, f, ensure_ascii=False)
    print("완료했습니다.")
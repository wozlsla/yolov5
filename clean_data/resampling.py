# coding:utf-8
import os
import json
import pandas as pd
from collections import OrderedDict


# 원본 annotation 파일들이 있는 경로 (TRAIN, VALID)
annoResampleDir = "/homedataset/aihub/train/songdo/labels/" # Songdo
# annoResampleDir = "/homedataset/aihub/valid/songdo/labels/" 
# annoResampleDir = "/homedataset/aihub/train/hanam/labels/" # Hanam
# annoResampleDir = "/homedataset/aihub/valid/hanam/labels/"

# anno_dir 내 annotation 파일 이름 리스트업
annoResampleList = os.listdir(annoResampleDir)
print(len(annoResampleList))
print(annoResampleList[:10])

# DF 정의하기
anno_dict_resample = {"01":0,"02":0,"03":0,"04":0,"05":0,"06":0,"07":0,"08":0,"09":0,"10":0,
     "10":0,"11":0,"12":0,"13":0,"14":0,"15":0,"16":0,"17":0,"18":0,"19":0,
     "20":0,"21":0,"22":0,"23":0,"24":0,"25":0,"26":0,"27":0,"28":0,"29":0,
     "30":0,"31":0,"32":0,"33":0,"34":0,"35":0,"36":0,"37":0,"38":0,"39":0,
     "40":0,"41":0,"42":0,"43":0,"44":0,"45":0}

# 안전보호구 5클래스(1,2,5,7,8)만 남기고 나머지 다 삭제하기
# 수정 후 json 파일 변경
# .DS_Store 파일이 간혹 생길때가 있습니다. 폴더 내에 해당 파일이 존재하면 오류가 발생합니다. 반드시 찾아서 삭제 후 진행하세요.
f = open("/home/dataset/train/5class_resampling.txt", 'w')

# Use Classes : 1.belt 5.boots 7.hardhat
remove_list = ["02","03","04","06","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25",
              "26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45"]


for anno in annoResampleList:
    try :
        with open(annoResampleDir + anno, encoding="utf-8-sig", errors="ignore") as json_file:
            jsonData = json.load(json_file)
    except : # .DS_Store가 있는지 확인하기 위해 작성, 일반적으로 mac Finder에는 해당 파일이 보이지 않으나 SFTP 시스템 등으로 보면 해당 파일이 있으니 삭제합니다.
        print(anno)

    imgPath = anno.replace(".json", ".jpg")
    df = pd.json_normalize(jsonData)
    filename = df["image.filename"][0]
    annoList = df["annotations"][0]
    # print(f"File name : {filename}")
        
    for i in annoList[:]:
        if i["class"] in remove_list:
            annoList.remove(i)
    
    if annoList : 
        for j in range(len(annoList)) : 
            item = annoList[j]["class"]
            # class imblance를 조정하기 위해서 현재는 Tao yolo에서 class_weight를 지원하지만, 애초에 전처리 과정에서 개수를 제한해 적당한 비율 맞추기
            # 해당 레이블 개수가 10000개를 이하이면
            if anno_dict_resample[item] < 50000 :
                anno_dict_resample[item] += 1
                # 레이블이 10000개를 넘기지 않을 때만 이미지명을 저장한다. 중복이 생기지만 추후에 제거
                f.write(filename+'\n')
        
    with open(annoResampleDir + anno, 'w', encoding="utf-8-sig", errors="ignore") as outfile:
        json.dump(jsonData, outfile)
        
f.close()

print(anno_dict_resample)

# 값(value)를 기준으로 정렬한 OrderedDict
ordered_dict = OrderedDict(sorted(anno_dict_resample.items(), key=lambda t:t[1], reverse=True))
print(ordered_dict)
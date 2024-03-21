## Data Processing (Yolo)  
AI 허브 데이터 전처리 예제  
https://velog.io/@moey920/AI-%ED%97%88%EB%B8%8C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%84%EC%B2%98%EB%A6%AC-%EC%98%88%EC%8B%9C 
<br/>

### 전처리
- cls_resampling.py  
  Sampling specific classes
- cls_distribution.py  
  Class sampling (Class Imbalance)
- pair_check_image.sh / pair_check.sh  
  Check pair files (img, ann)  
<br/>
- cls_convert.py  
  Convert Class - ex, 0 to 1 
- ann_merge.py  
  Merge label contents - ex, detect_1(class person), detect_2(class_ppe)
<br/>

### Annotation 변환  
AI hub -> COCO -> Yolov5
- to_coco.py  
  AI Hub ann -> COCO ann
- to_yolo.py  
  COCO ann -> Yolov5 ann
- (Person Only) coco_to_yolo.py  
  COCO ann -> Yolov5 ann, Person class only  
  <br/>
최종: Yolov5 format
<br/>
<br/>


## File Processing
### Rename
-  rename.py   
이름 쌍(img, label)으로 맞춰서 변경
- rename_replace.py  
이름 Replace : v1_img -> v2_img
- rename_order.py -> sampling_by_steps.py  
Stream 이미지 시간의 흐름대로 보여주려고 - stream_00.jpg 형식, 번호는 그대로 두고 이름만 변경 (natsorted X)  
파일 순서가 python 에서는 1, 10, 11, 12, ..., 2, 20, ...  
 
### Split Dataset
- split_dataset.py    
  외 : sklearn - train_test_split() / splitfolders
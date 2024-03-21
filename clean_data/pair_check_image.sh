#!/bin/bash
# label(.txt) 과 쌍이 안맞는 image(.jpg)만 체크해서 제거 (전체 이미지 데이터셋에 대해 수행해야함)
# $ bash pair_check_image.sh ./images ./labels
# $ bash pair_check_image.sh [제거] [기준]


for img in $1/*.jpg # rm-img
# for ann in $1/*.txt # rm-txt
# for ann in $1/*.json
do


kitti_name=$2/$(basename $img .jpg).json # rm-img, st-json
# kitti_name=$2/$(basename $img .jpg).txt # rm-img, st-txt
# kitti_name=$2/$(basename $ann .txt).jpg # rm-txt, st-img
# kitti_name=$2/$(basename $ann .json).jpg
kitti_name=$2/$(basename $ann .txt).txt # txt-txt
# kitti_name=$2/$(basename $img .jpg).jpg # img-img
# kitti_name=$2/$(basename $img .JPG).txt
# kitti_name=$2/$(basename $ann .txt).JPG # Mask_ai format


if [  ! -f  $kitti_name ]; then
# if [ -f  $kitti_name ]; then

echo "$kitti_name not exist, will remove that image pair."
rm $img
# cp -r $img /home/dataset/images/
# cp -r $ann /home/dataset/labels/

fi
done

echo "$1: $(ls $1|wc -l)"
echo "$2: $(ls $2|wc -l)"
echo Done!

#!/bin/bash
# 레이블->이미지 뿐만 아니라, 이미지->레이블 쌍도 검사
# $ bash pair_check.sh ~/images ~/labels

for img in $1/*.jpg
do
kitti_name=$2/$(basename $img .jpg).txt
if [  ! -f  $kitti_name ]; then
echo "$kitti_name not exist, will remove that image pair."
rm $img
fi
done

for ann in $2/*.txt
do
img_name=$1/$(basename $ann .txt).jpg
if [ ! -f $img_name ]; then
echo "$img_name not exist, will remove that label pair."
rm $ann
fi
done

echo "$1: $(ls $1|wc -l)"
echo "$2: $(ls $2|wc -l)"
echo Done!
#!/usr/bin/env python
#coding=utf-8
import cv2
import os
import glob

image_dir = r"/home/viplab/桌面/MVCNN_dataset/single_off_samples/3d_model"

file_glob = os.path.join(image_dir,'*',"stl","*.stl")
print(file_glob)

file_list = []
file_list.extend(glob.glob(file_glob))
print(file_list)
for i in range(len(file_list)):
    x=file_list[i].split('/')
    print(x)
    newPwd='.'+'/'+'/'.join(str(j) for j in x[5:])
    print(newPwd)
    f = open(r'/home/viplab/桌面/MVCNN_dataset/single_off_samples/vip_model_list_stl.txt','a')
    f.write(newPwd+'\n')
#!/usr/bin/env python
# -*- coding=utf-8 -*-




import cv2
import os
path1 = "C:/Users/xlh/Desktop/4.16"
# video_list = []

i = 11043

def file_name(file_dir,i):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            # video = video_list.append(os.path.splitext(file)[0])
            # print video
            video_file = file
            print video_file
            cap = cv2.VideoCapture('C:/Users/xlh/Desktop/4.16/%s'% video_file) #创建一个视频获取对象
            flag = 0

            while (cap.isOpened()):
                # cap.set(cv2.CAP_PROP_POS_MSEC,flag)#设置时间标记
                # print(i)
                cap.set(cv2.CAP_PROP_POS_FRAMES,flag) #设置帧数标记
                ret,im = cap.read()#获取图像
                # cv2.waitKey(2000)#延时
                # cv2.imshow('a',im)#显示图像，用在循环中可以播放视频
                cv2.imwrite('C:/Users/xlh/Desktop/oo1/ %s.jpg'%i,im)#保存图片
                flag += 8  # 设置间隔
                i += 1
                print i
                if not ret:
                    break

if __name__ == '__main__':
    file_name(path1,i)


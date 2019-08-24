#!/usr/bin/env python
# -*- coding=utf-8 -*-


import os
import cv2


# 遍历指定目录，显示目录下的所有文件名
def CropImage4File(filepath, destpath):
    pathDir = os.listdir(filepath)  # 列出文件路径中的所有路径或文件
    for allDir in pathDir:
        child = os.path.join(filepath, allDir)
        dest = os.path.join(destpath, allDir)
        image = cv2.imread(child)
        print(child)
        if image is None:
            os.remove(child)
            continue
        sp = image.shape  # 获取图像形状：返回【行数值，列数值】列表
        if sp == 0:
            os.remove(child)
            continue
        # print image.shape
        sz1 = sp[0]  # 图像的高度（行 范围）
        sz2 = sp[1]  # 图像的宽度（列 范围）
        # sz3 = sp[2]                #像素值由【RGB】三原色组成
        # 你想对文件的操作
        if sz1 >= 480 and sz2 >= 640:
            a = int(sz1 / 2 - 240)  # x start
            b = int(sz1 / 2 + 240)  # x end
            c = int(sz2 / 2 - 320)  # y start
            d = int(sz2 / 2 + 320)  # y end
            cropImg = image[a:b, c:d]
            print child
            cv2.imwrite(dest, cropImg)
        else:
            pass
        # 裁剪图像
        # 写入图像路径


if __name__ == '__main__':
    filepath = "C:/Users/xlh/Desktop/040301"  # 源图像
    destpath = "C:/Users/xlh/Desktop/bird0403"# resized images saved here
    CropImage4File(filepath, destpath)

#!/usr/bin/env python
# -*- coding=utf-8 -*-


# -*- coding: utf-8 -*-
import os


path1 = "C:/Users/xlh/Desktop/ii"

def file_name(file_dir):
    jpg_list = []
    txt_list = []
    # jpeg_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                jpg_list.append(os.path.splitext(file)[0])
            elif os.path.splitext(file)[1] == '.txt':
                txt_list.append(os.path.splitext(file)[0])


    diff = set(txt_list).difference(set(jpg_list))  # 差集，在a中但不在b中的元素
    print(len(diff))
    for name in diff:
        print("no jpg", name + ".txt")

    diff2 = set(jpg_list).difference(set(txt_list))  # 差集，在b中但不在a中的元素
    print(len(diff2))
    for name in diff2:
        # print("no jpg", name + ".txt")
        child= name + ".jpg"
        # child2 = name + ".jpeg"
        child1 = os.path.join(path1, child)
        os.remove(child1)
    return jpg_list,txt_list

    # 其中os.path.splitext()函数将路径拆分为文件名+扩展名

if __name__ == '__main__':

    file_name(path1)


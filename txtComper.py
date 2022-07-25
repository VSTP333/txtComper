#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
file1 为之前的文件
file2 为现在的文件  需要比对file2中 file1没有的

"""
def file_same():
    str1 = []
    file1 = open("C:\\Users\\Administrator\\Desktop\\zichan\\ip_old.txt", "r", encoding="utf-8")
    for line in file1.readlines():  # 读取第一个文件
        str1.append(line.replace("\n", ""))

    str2 = []
    file2 = open("C:\\Users\\Administrator\\Desktop\\zichan\\ip_new.txt", "r", encoding="utf-8")
    for line in file2.readlines():  # 读取第二个文件
        str2.append(line.replace("\n", ""))

    str_dump = []
    a = 0
    for line in str2:
        if line  not in str1:
            str_dump.append(line)  # 将两个文件重复的内容取出来
            print(line)  # 将重复的内容输出
            a = a+1
            #print("*"*80)


if __name__ == "__main__":
    file_same()

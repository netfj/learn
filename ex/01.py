#coding:utf-8
# @Info: 
# @Author:Netfj@sina.com @File:01.py @Time:2019/3/1 14:31

try:
    fh = open("testfile1", "r")

except IOError as e:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容 成功")
    fh.close()
    

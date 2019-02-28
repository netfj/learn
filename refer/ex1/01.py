#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   01.py 
time:   2019/2/27.18:44
"""


def main():
    import ctypes
    ctypes.windll.user32.MessageBoxA(
        0, u"点击确定".encode('gb2312'),u'信息'.encode('gb2312'), 0)
    ctypes.windll.user32.MessageBoxA(
        0, u"点击确定".encode('gb2312'),u'信息'.encode('gb2312'), 1)
    ctypes.windll.user32.MessageBoxA(
        0, u"点击确定".encode('gb2312'),u'信息'.encode('gb2312'), 2)
    ctypes.windll.user32.MessageBoxA(
        0, u"点击确定".encode('gb2312'),u'信息'.encode('gb2312'), 3)
    ctypes.windll.user32.MessageBoxA(
        0, u"点击确定".encode('gb2312'),u'信息'.encode('gb2312'), 4)
    ctypes.windll.user32.MessageBoxA(
        0, u"点击确定".encode('gb2312'),u'信息'.encode('gb2312'), 5)
    ctypes.windll.user32.MessageBoxA(
        0, u"点击确定".encode('gb2312'),u'信息'.encode('gb2312'), 6)
    ctypes.windll.user32.MessageBoxA(
        0, u"点击确定".encode('gb2312'),u'信息'.encode('gb2312'), 7)


if __name__ == "__main__":
    main()


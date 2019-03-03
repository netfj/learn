#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   02.py 
time:   2019/3/3.19:31
"""


if not ('=' in 'info="abcd"'):
    print('=========')
else:
    print('~~~~~~~~')

import ctypes
player = ctypes.windll.kernel32
player.Beep(3000,500)

import winsound
duration = 600  # millisecond
freq = 440  # Hz
winsound.Beep(freq, duration)


for i in range(0,10000,100):
    player.Beep(i, 500)
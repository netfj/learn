#coding:utf-8
# @Info: 
# @Author:Netfj@sina.com @File:07_position.py @Time:2019/2/25 15:56

import pyautogui
####显示鼠标坐标位置,给出这个像素的RGB颜色

import pyautogui,time
print('Press Ctrl-C to quit')
try:
    while  True:
        x,y=pyautogui.position()
        positionStr='X: '+str(x).rjust(4)+' Y: '+str(y).rjust(4)
        pixelColor=pyautogui.screenshot().getpixel((x,y))

        positionStr +='\nRGB: ('+str(pixelColor[0]).rjust(3)
        positionStr +=', '+str(pixelColor[1]).rjust(3)
        positionStr +=', '+str(pixelColor[2]).rjust(3) +')'

        print(positionStr)
        print('\b'*len(positionStr))

        time.sleep(1)

except KeyboardInterrupt:
    print('\nDone.')
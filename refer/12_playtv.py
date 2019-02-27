#coding:utf-8
"""
info:   观看视频
author: NetFj@sina.com
file:   12_playtv.py.py 
time:   2019/2/26.18:33
"""

import time,webbrowser,pyautogui,random

class study():
    def __init__(self):     #入口：定义软件名称，默认网站
        self.brower = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        self.site_name = r'https://www.xuexi.cn/'

    def open_site(self):    # 打开一个网站
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(self.brower))
        webbrowser.get('chrome').open(self.site_name, new=1, autoraise=True)
        time.sleep(5)

        #窗口最大化
        pyautogui.keyDown('alt')
        pyautogui.press('space')
        pyautogui.press('x')
        pyautogui.keyUp('alt')

        #定位到页首
        pyautogui.hotkey('ctrl','home')
        time.sleep(2)

    def open_link(self,x,y):    #打开指定位置的链接
        time.sleep(1)
        pyautogui.click(x, y, button='left')
        time.sleep(3)

    def open_tv_xwlb_old(self):
        self.open_link(620, 513)
        pyautogui.press('pagedown', presses=2)
        pyautogui.moveTo(452, 219)
        time.sleep(5)
        pyautogui.moveTo(1114, 278)
        time.sleep(3)
        pyautogui.click(button='left')
        time.sleep(5)
        self.open_link(417, 850)
        pyautogui.press('down', presses=5)

    def open_tv_short(self):
        print('播放短片开始...')
        self.open_site()
        self.open_link(620, 513)
        pyautogui.press('pagedown', presses=2)
        self.open_link(460, 500)

        ts = 20+random.randint(0,30)

        self.open_link(435,850)
        pyautogui.press('down', presses=10)
        time.sleep(ts)
        pyautogui.hotkey('ctrl', 'w')  # 关闭

        self.open_link(435, 890)
        pyautogui.press('down', presses=10)
        time.sleep(ts)
        pyautogui.hotkey('ctrl', 'w')  # 关闭

        self.open_link(435, 930)
        pyautogui.press('down', presses=10)
        time.sleep(ts)
        pyautogui.hotkey('ctrl', 'w')  # 关闭

        self.open_link(435, 970)
        pyautogui.press('down', presses=10)
        time.sleep(ts)
        pyautogui.hotkey('ctrl', 'w')  # 关闭
        pyautogui.hotkey('ctrl', 'w')  # 关闭
        pyautogui.hotkey('ctrl', 'w')  # 关闭
        time.sleep(3)
        print('播放短片...结束!')


    def open_tv_xwlb(self):
        print('播放新闻联播开始...')
        self.open_link(620, 513)
        pyautogui.press('pagedown', presses=2)
        self.open_link(460, 500)
        self.open_link(1040, 795)
        self.open_link(405, 850)
        pyautogui.press('down', presses=5)
        print('将要播放30分钟...')
        time.sleep(30*60+random.randint(0,100))     #播放30多分钟
        pyautogui.hotkey('ctrl', 'w')  # 关闭
        pyautogui.hotkey('ctrl', 'w')  # 关闭
        pyautogui.hotkey('ctrl', 'w')  # 关闭
        pyautogui.hotkey('ctrl', 'w')  # 关闭
        time.sleep(3)
        print('播放新闻联播...结束!')



def main():
    stu = study()
    stu.open_tv_short()
    stu.open_tv_xwlb()


if __name__ == "__main__":
    main()


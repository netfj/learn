#coding:utf-8
# @Info: 每隔 n 秒移动下鼠标
# @Author:Netfj@sina.com @File:08.py @Time:2019/2/25 17:29

import pyautogui,time,random,webbrowser

print('阅读新闻开始...')

def time_set():
    #设置随机时间
    t_ready = 2 + random.randint(0, 3)
    t_ready_click = 2 +random.randint(0, 5)
    t_read = 180 +random.randint(0, 120)
    return (t_ready,t_ready_click,t_read)

#打开网站
def open_site(site_name):
    chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
    webbrowser.get('chrome').open(site_name,new=1,autoraise=True)
    time.sleep(5)
    pyautogui.keyDown('alt')
    pyautogui.press('space')
    pyautogui.press('x')
    pyautogui.keyUp('alt')
    time.sleep(2)

# 头条
def read_1st():
    #获取控制时间
    t = time_set()
    t_ready = t[0]
    t_ready_click = t[1]
    t_read = t[2]

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'home')    #定位到页首
    time.sleep(t_ready)                 #等待
    pyautogui.moveTo(878,636)           #定位到头条
    time.sleep(t_ready_click)           #等待
    pyautogui.click(button='left')      #左击打开
    time.sleep(1)

    #开始阅读
    pyautogui.hotkey('pagedown')        #翻页
    key_down()                          #下翻几行
    time.sleep(t_read)                  #阅读时间
    pyautogui.hotkey('ctrl','w')        #关闭
    time.sleep(1)



#要闻
def read_news(x,y):
    #获取控制时间
    t = time_set()
    t_ready = t[0]
    t_ready_click = t[1]
    t_read = t[2]

    #随机化点
    x = x + random.randint(0,30)
    y = y + random.randint(-2,2)

    time.sleep(t_ready)
    pyautogui.moveTo(x, y)
    time.sleep(t_ready_click)
    pyautogui.click(button='left')      #打开
    time.sleep(1)

    # 开始阅读
    pyautogui.hotkey('pagedown')        #翻页
    key_down()                          #下翻几行
    time.sleep(t_read)                  #阅读时间
    pyautogui.hotkey('ctrl','w')        #关闭
    time.sleep(1)

# 下翻几行
def key_down():
    for i in range(5+ random.randint(0, 6) ):
        time.sleep(1)
        pyautogui.press('down')


#打开网站
open_site('https://www.xuexi.cn')

#头条
read_1st()

#要闻
time.sleep(2)
pyautogui.hotkey('pagedown')
read_news(366,786)
read_news(366,838)
read_news(366,882)
read_news(366,940)

read_news(800,786)
read_news(800,838)
read_news(800,882)
read_news(800,940)

pyautogui.hotkey('ctrl', 'w')  # 关闭

print('阅读新闻...结束')

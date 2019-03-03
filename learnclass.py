#coding:utf-8
# @Info: learn a site class
# @Author:Netfj@sina.com @File:learnclass.py.py @Time:2019/2/27 12:28

import logging, time, webbrowser, random, pyautogui

logging.basicConfig(filename='runinfo.log',
                    level=logging.DEBUG,
                    format="【%(asctime)s】%(message)s",
                    datefmt="%m.%d.%H:%M:%S")

class learn():
    cursor_x=0
    cursor_y=0
    runstep_name = 'runstep.ini'
    site_name = 'www.baidu.com'
    brower_file = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser_register = 'web_reg_name'

    def __init__(self):
        pass

    def run(self):
        with open(self.runstep_name) as f:
            t = f.readlines()
            m = len(t)
        for i in range(m):
            item = t[i].strip('\n')     # 去除尾部的换行符
            p = item.find('#')          # 求 # 所在的位置
            if p>=0 : item = item[0:p]   # 去除 # 之后的字符
            item = item.strip()         # 去除两边 空格
            if item == '': continue     # 跳过空行

            # 日志：读到的命令行
            self.debug('Line: {0}; Command: {1}'.format(i+1,item))
            print(' '*50,i+1,'|',item)

            if item.replace(' ','').lower() == 'action=stop': break     # 遇stop标识时，终止进行,【标识：处理action=stop】

            # 记录信息类命令行: 单行
            if not ('=' in item):
                self.info(item)

            # 记录信息类命令行: info = '.....'
            if item.replace(' ','').lower()[:5] == 'info=':
                self.info(item[item.find('=')+1:])      #执行 self.indo() , 参数：“=”右边的部分
                continue

            # 分类处理命令：主要包括坐标、鼠标、键盘
            lt = item.split('=')  # 解析
            if len(lt)==2:
                lt[0] = lt[0].replace(' ', '').lower()  # 等号左边：去空格，变小写
                lt[1] = lt[1].strip()                   # 等号右边：去两侧的空格
                command = 'self.'+lt[0]+r'("'+lt[1]+'")'
                print(command)
                try:
                    eval(command)
                except TypeError as e:
                    self.info('Wrong command: '+command)
                    self.debug(e)
                else:
                    pass
        self.info('Script run finished.')

    def debug(self,aru):
        logging.debug(aru)
        # print(aru)

    def x(self,aru):
        self.cursor_x = int(aru)
        logging.debug('x='+aru)

    def y(self,aru):
        self.cursor_y = int(aru)
        logging.debug('y='+aru)

    def setx(self, aru):
        self.cursor_x = self.cursor_x + int(aru)
        logging.debug('x=x+'+aru+' --> x='+str(self.cursor_x))

    def sety(self, aru):
        self.cursor_y = self.cursor_y + int(aru)
        logging.debug('y=y+'+aru+' --> y='+str(self.cursor_y))

    def info(self,aru):
        logging.info(aru.strip())       # 去空格，写入日志

    def site(self, aru):
        self.debug('Set site: '+aru)
        self.site_name = aru

    def brower(self, aru):
        self.debug('Set brower: ' + aru)
        self.brower_file = aru

    def action(self, aru):
        '''
            action=opensite
            注意：action=stop 不在此执行，在读入runstep时就处理掉了 【标识：处理action=stop】
        '''
        aru = aru.replace(' ','').lower()   #去空格变小写
        eval('self.' + aru +'()')   #导入 action 对应函数

    def opensite(self):
        self.debug('Open site: '+self.site_name )

        self.webbrowser_register = 'webname'+str(random.randint(1,200000))
        webbrowser.register(self.webbrowser_register, None, webbrowser.BackgroundBrowser(self.brower_file))
        webbrowser.get(self.webbrowser_register).open(self.site_name.strip(), new=1, autoraise=True)

        self.debug('webbrowser.register: ' + self.webbrowser_register)
        time.sleep(5)

    def mouse(self,aru):
        '''
            mouse=leftclick@(x,y)
            mouse=rightclick@(x,y)
        '''
        aru = aru.replace(' ', '').lower()  # 去空格变小写
        if '@' in aru:
            x,y = self.cursor_x, self.cursor_y
            lt = aru.split('@')
            cm = 'self.' + lt[0] + lt[1]
            eval(cm)  # 导入 mouse 对应函数

    def leftclick(self, x=-9, y=-9):
        self.debug('left click ...({0},{1})'.format(x,y))
        try:
            pyautogui.click(x, y, button='left')
        except TypeError as e:
            self.debug(e)
        else:
            pass

        time.sleep(3)

    def rightclick(self, x=-9, y=-9):
        self.debug('right click ...({0},{1})'.format(x,y))
        pyautogui.click(x, y, button='right')
        time.sleep(3)

    def keyboard(self,aru):
        '''
            # Keyboard letter or press hotkey
            keyboard=pageup
            keyboard=pageup*2   # Press pageup 2 times
            keyboard=pagedown
            keyboard=pagedown*3
            keyboard=up
            keyboard=up*5
            keyboard=down
            keyboard=down*6
            keyboard=Ctrl+W     #Press Ctrl and W
            keyboard=Alt+F4
        '''
        aru = aru.replace(' ', '').lower()  # 去空格变小写
        self.debug('Input: '+aru)
        if '*' in aru:
            # 重复按
            kb = aru.split('*')
            if len(kb)==2:
                self.debug('-->Press: {0} {1} times'.format(kb[0],kb[1]))
                pyautogui.press(kb[0],presses=int(kb[1]))

        elif '+' in aru:
            # 组合键
            kb = aru.split('+')
            if len(kb) == 2:
                self.debug('-->Press: {0} + {1}'.format(kb[0], kb[1]))
                pyautogui.hotkey(kb[0],kb[1])
        else:
            self.debug('-->Press: {0}'.format(aru))
            pyautogui.press(aru)

    def sleep(self,aru):
        if aru.isdigit():
            sleeptime = int(aru)
            msg = '(Digit)'
        elif 'random' in aru.lower():
            aru = aru.replace('random','random.randint')
            sleeptime = eval(aru.lower())
            msg = '(random)'
        else:
            sleeptime = 0
            msg = ''
        self.debug('Sleep {0} seconds {1}'.format(sleeptime,msg))
        time.sleep(sleeptime)


if __name__ == '__main__':
    le = learn()
    le.run()

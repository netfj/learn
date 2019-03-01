#coding:utf-8
# @Info: learn a site class
# @Author:Netfj@sina.com @File:learnclass.py.py @Time:2019/2/27 12:28

import logging, time, webbrowser,random

logging.basicConfig(filename='runinfo.log',
                    level=logging.DEBUG,
                    format="【%(asctime)s】%(message)s",
                    datefmt="%m.%d.%H:%M")


class learn():
    cursor_x=0
    cursor_y=0
    runstep_name = 'runstep.ini'
    site_name = 'www.baidu.com'
    brower = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser_register = 'web_reg_name'

    def __init__(self):
        pass

    def run(self):
        with open(self.runstep_name) as f:
            t = f.readlines()
            m = len(t)
        for i in range(26):
            item = t[i].strip('\n')     # 去除尾部的换行符
            p = item.find('#')          # 求 # 所在的位置
            if p>=0 : item = item[0:p]   # 去除 # 之后的字符
            item = item.strip()         # 去除两边字符串
            if item == '': continue
            item = item.split('=')

            print(' '*50,i+1,'|',item)

            if len(item)==1:
                self.info(item[0])
                continue
            elif len(item)==2:
                command = 'self.'+item[0]+r'("'+item[1]+'")'
                eval(command)

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
        logging.debug('x=x+'+aru+' -->  x='+str(self.cursor_x))

    def sety(self, aru):
        self.cursor_y = self.cursor_y + int(aru)
        logging.debug('y=y+'+aru+' -->  y='+str(self.cursor_y))

    def info(self,aru):
        logging.info(aru)

    def site(self, aru):
        self.debug('Set site: '+aru)
        self.site_name = aru

    def brower(self, aru):
        self.debug('Set brower: ' + aru)
        self.brower = aru

    def action(self, aru):
        eval('self.' + aru +'()')   #导入 action 对应函数

    def opensite(self):
        self.debug('Open site: '+self.site_name )
        self.webbrowser_register = 'web_name'+str(random.randint(1,200000))
        webbrowser.register(self.webbrowser_register, None, webbrowser.BackgroundBrowser(self.brower))
        webbrowser.get(self.webbrowser_register).open(self.site_name, new=1, autoraise=True)
        self.debug('webbrowser.register: ' + self.webbrowser_register)
        time.sleep(5)

    def mouse(self,aru):
        eval('self.' + aru + '()')  # 导入 mouse 对应函数

    def rightclick(self):
        self.debug('right click ...')

    def leftclick(self):
        self.debug('left click ...')

    def middleclick(self):
        self.debug('middle click ...')


if __name__ == '__main__':
    le = learn()
    le.run()
    print(le.cursor_x,le.cursor_y)

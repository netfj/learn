#coding:utf-8
# @Info: learn a site class
# @Author:Netfj@sina.com @File:learnclass.py.py @Time:2019/2/27 12:28

import logging, time

logging.basicConfig(filename='runinfo.log',
                    level=logging.DEBUG,
                    format="【%(asctime)s】%(message)s",
                    datefmt="%m.%d.%H:%M")


class learn():
    x=0
    y=0
    runstep_name = 'runstep.ini'
    site_name = 'www.baidu.com'
    brower_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    

    def __init__(self):
        pass

    def read_runstep(self):
        with open(self.runstep_name) as f:
            t = f.readlines()
            m = len(t)
        for i in range(11):
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
        print(aru)

    def info(self,aru):
        logging.info(aru)

    def site(self, aru):
        self.debug('Set site: '+aru)
        self.site_name = aru

    def brower(self, aru):
        self.debug('Set brower: ' + aru)
        self.brower_path = aru

    def action(self, aru):
        print(aru)


if __name__ == '__main__':

    le = learn()
    le.read_runstep()

    print('====================')
    print(le.site_name)
    print(le.brower_path)

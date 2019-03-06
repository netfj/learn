#coding:utf-8
# @Info: 
# @Author:Netfj@sina.com @File:main.py.py @Time:2019/3/5 16:22

def main():
    import learnclass
    learn = learnclass.learn(runstep_name='runstep_ltc.ini',runtime = '!test',loglevel='DEBUG')
    learn.demo()
    learn.run()


if __name__ == "__main__":
    main()
    

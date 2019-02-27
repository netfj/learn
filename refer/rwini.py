
class RwConfig():       #读写配置文件
    def __init__(self,config_name='config.ini'):
        config_name=str(config_name)
        import configparser
        self.config_name = config_name
        self.cf = configparser.ConfigParser()
        self.cf.read(self.config_name)

    #读取一个配置
    def get2(self,section='default',option='default'):
        section,option=str(section),str(option)
        try:
            return self.cf.get(section,option)
        except:
            return None
    def get(self,*args):
        if len(args)==1:
            args = ('default',args[0])
        elif len(args)==0:
            args = ('default', 'default')
        return self.get2(args[0],args[1])

    #读取所有章节：返回值：包含章节值的列表
    def get_sections(self):
        return self.cf.sections()

    #判断一个章节是否存在：返回值：True-有；Flase-无
    def section_is_exist(self,sec):
        sec=str(sec)
        return sec in self.get_sections()

    #增加一个章节：返回值：True-成功；Flase-失败
    def add_section(self,sec):
        sec=str(sec)
        if self.section_is_exist(sec): return True   #存在则终止
        self.cf.add_section(sec)
        with open(self.config_name, 'w') as fw:
            self.cf.write(fw)  # 写入
        return self.section_is_exist(sec)

    # 删除一个章节：返回值：True-成功；Flase-失败
    def remove_section(self,sec):
        sec=str(sec)
        if self.section_is_exist(sec)==False: return True  #不存在则终止
        self.cf.remove_section(sec)
        with open(self.config_name, 'w') as fw:
            self.cf.write(fw)  # 写入
        return not self.section_is_exist(sec)

    #读取一个章节下的所有配置项（键）：返回值：列表
    def get_option(self,sec='default'):
        sec = str(sec)
        if not self.section_is_exist(sec): return [sec+':该章节不存在']
        return self.cf.options(sec)

    #读取一个章节下的所有配置（键和值）：返回值：字典
    def get_items(self,sec='default'):
        sec = str(sec)
        if not self.section_is_exist(sec): return [(sec,'该章节不存在')]
        return self.cf.items(sec)

    #判决一个配置项是否存在：返回值：True-存在；Flase-不存在
    def option_is_exist(self,sec,opt):
        sec, opt = str(sec), str(opt)
        return opt in self.get_option(sec)

    #增加、修改配置：返回值：True-成功；Flase-失败
    def set3(self,sec,opt,val):
        sec, opt, val = str(sec), str(opt), str(val)
        if self.add_section(sec)==False : return False
        self.cf.set(sec,opt,val)
        with open(self.config_name, 'w') as fw:
            self.cf.write(fw)  # 写入
        return self.get(sec,opt)==val
    def set(self,*args):
        n=len(args)
        if   n==0 : return '-1.参数不足，至少1个（值）'
        elif n==1 : args=['default','default',args[0]]
        elif n==2 : args=['default',args[0],args[1]]
        elif n==3 : pass
        elif n>3  : return '-2.参数过多，最多3个（章节名、键、值）'
        return self.set3(args[0],args[1],args[2])

    #删除一个配置
    def remove_option2(self,sec,opt):
        sec, opt = str(sec), str(opt)
        self.cf.remove_option(sec,opt)
        with open(self.config_name, 'w') as fw:
            self.cf.write(fw)  # 写入

    #读取所有配置，返回值：一个集合
    def get_all(self):
        re = {}
        section_all = self.get_sections()
        for s in section_all :
            opts = self.get_items(s)
            re[s]=opts
        return re

    def help(self):
        text = '''
            # 示例：直接复制运行即可
            # 其它模块时注意引入：
            # from rwini import RwConfig
            
            rwini = RwConfig('test.ini')
            
            #写入配置(创建测试用配置文件)
            rwini.set('这是传递1个参数的测试')
            rwini.set('objective','这是传递2个参数的测试')
            rwini.set('MyFistSection','information','这是传递3个参数的测试')
            for n in range(5):
                rwini.set('TestSection'+str(n), 'name', 'Tom')
                rwini.set('TestSection'+str(n), 'age', n*10)
                rwini.set('TestSection'+str(n), 'man', 'Ture')
            
            print('【读取配置】')
            print('不传递参数（默认章节default，键default)：\n'
                  'default =', rwini.get())
            print('传递一个参数（默认章节default）：\n'
                  'objective =', rwini.get('objective'))
            print('传递两个参数：\n'
                  'information =', rwini.get('MyFistSection','information'))
            print('读取不存在的配置: \n', rwini.get('aaabbbccc'))
            
            print('【查看所有的章节】')
            print(rwini.get_sections())
            
            print('【查看某章节下的所有键】')
            print('不传递参数（默认章节default）：\n', rwini.get_option())
            print('传递一个参数：\n', rwini.get_option('MyFistSection'))
            
            print('【查看某章节下的所有键对】')
            print(rwini.get_items('default'))
            
            print('【读取全部配置表】')
            print(rwini.get_all())
            '''
        return text


if __name__ == "__main__":
    # 示例：直接复制运行即可
    # 其它模块时注意引入：
    # from rwini import RwConfig

    rwini = RwConfig('test.ini')

    # 写入配置(创建测试用配置文件)
    rwini.set('这是传递1个参数的测试')
    rwini.set('objective', '这是传递2个参数的测试')
    rwini.set('MyFistSection', 'information', '这是传递3个参数的测试')
    for n in range(5):
        rwini.set('TestSection' + str(n), 'name', 'Tom')
        rwini.set('TestSection' + str(n), 'age', n * 10)
        rwini.set('TestSection' + str(n), 'man', 'Ture')

    print('【读取配置】')
    print('不传递参数（默认章节default，键default)：\n'
          'default =', rwini.get())
    print('传递一个参数（默认章节default）：\n'
          'objective =', rwini.get('objective'))
    print('传递两个参数：\n'
          'information =', rwini.get('MyFistSection', 'information'))
    print('读取不存在的配置: \n', rwini.get('aaabbbccc'))

    print('【查看所有的章节】')
    print(rwini.get_sections())

    print('【查看某章节下的所有键】')
    print('不传递参数（默认章节default）：\n', rwini.get_option())
    print('传递一个参数：\n', rwini.get_option('MyFistSection'))

    print('【查看某章节下的所有键对】')
    print(rwini.get_items('default'))

    print('【读取全部配置表】')
    print(rwini.get_all())
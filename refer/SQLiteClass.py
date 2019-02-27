#coding:utf-8
'''
名称：SQLite3 操作类 ver 0.2  2018-11-4
功能：SQLite 数据库、表的建立，记录的增删改查
作者：NetFj@sina.com
目录：
    第1部分：数据库
    第2部分：表
    第3部分：字段（列）
    第4部分：记录（1.增；2.删；3.改；4.查）
    第5部分：视图
    第6部分：索引
    第7部分：事务
'''

import sqlite3
import logging
import time

def log_config(log_name='SQLiteRunInfo.log'):
    logging.basicConfig(filename=log_name,
                        level=logging.DEBUG,
                        format="%(funcName)s(%(lineno)d)[%(levelname)s]%(message)s")
    logging.debug(time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime()) + '\n模块或函数名(行号)[日志类型]日志信息')
    logging.debug('日志设置完成：'+log_name)

class Dbt:
    '''
    操作sqlite数据库的类
    '''

    ###  第 1 部分：数据库  #############################

    def __init__(self):
        pass

    def database_connect(self,DatabaseName='test.db'):
        try:
            self.connect = sqlite3.connect(DatabaseName)    #连接数据库，没有则建立
            self.cursor = self.connect.cursor()  # 取得游标
            logging.debug("Opened database successfully:%s" % DatabaseName)
            return True
        except Exception as e:
            logging.error('Open database error: ' + repr(e))
            return False
        finally:
            pass

    def database_disconnect(self):
        '''断开数据库'''
        self.connect.close()

    #查询数据库中的所有表，返回值：列表（性质，表名，表名，rootpage，建表命令）
    def tables_all_get(self):
        '''查询表'''
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        return self.cursor.fetchall()

        ###  第 2 部分：表   ###################

    def teble_is_exist(self, table_name):        #判断一个表是否存在
        query = "SELECT count(*) FROM sqlite_master " \
                "WHERE type='table' AND name='%s' ;" % table_name
        self.cursor.execute(query)
        n = self.cursor.fetchone()[0]  # n=0时不存在
        if n == 0:
            # logging.debug('Table %s is NOT exist' % table_name)
            return False
        else:
            # logging.debug('Table %s is exist' % table_name)
            return True

    # 删除一个表
    def table_drop(self, table_name):
        ''' 删除表 '''
        if table_name == None:
            msg = 'Reference: .table_drop(table_name)'
            logging.error('Table name is losted !\n ' + msg)
            return False
        if self.teble_is_exist(table_name) == False:
            return True
        sql_command = 'drop table %s' % table_name
        try:
            self.cursor.execute(sql_command)
            logging.debug('Drop table succesfull ! (%s)' % sql_command)
            return True
        except:
            logging.error('Drop table fail ! (%s)' % sql_command)
            return False

    # 变更表名，给表改名
    def table_rename(self, name_old, name_new):
        '''重命名一个表'''
        if name_new == None or name_old == None:
            msg = 'Reference: .TableRname(name_old,name_new)'
            logging.error('Table name is losted !\n ' + msg)
            return False
        if self.teble_is_exist(name_old) == False:
            logging.error('Table is NOT exist !')
            return False
        if self.teble_is_exist(name_new):
            logging.error('Table (new name) already is exist !')
            return False
        sql_command = 'alter table %s rename to %s' % \
                      (name_old, name_new)
        try:
            self.cursor.execute(sql_command)
            self.connect.commit()
            logging.debug('Table Rename sucessful ! (%s)' % sql_command)
            return True
        except:
            logging.error('Table Rename fail ! (%s)' % sql_command)
            return False

    # 创建一个表，示例：
    # mydbt.table_create('tb1',['ID Integer PRIMARY KEY autoincrement','name text','age int'])
    def table_create(self,
                     table_name='test_user',
                     column_list=['ID Integer PRIMARY KEY autoincrement',
                                  'name   text', 'age int']):
        if self.teble_is_exist(table_name):
            logging.debug('表已经存在:'+ table_name)
            return True
        if len(column_list) == 0:
            logging.WARNING('建表失败，没有传递字段参数列表：'+table_name)
            return False
        try:
            sql = 'create table '+table_name+' ('
            for x in column_list:
                sql = sql+ x +','
            sql = sql.rstrip(',') + ');'
            logging.debug(sql)
            self.cursor.execute(sql)
            self.connect.commit()
            logging.debug("Table created done："+sql)
        except:
            logging.debug("Table created error: "+sql)
            return False
        if self.teble_is_exist(table_name):
            logging.debug('Create table successfully !')
            return True

    # 查询表的结构
    def table_structure_get(self, table_name=None):
        '''查询表结构'''
        if table_name == None:
            msg = '需要一个参数：表名'
            logging.error(msg)
            return [msg]
        if self.teble_is_exist(table_name) == False:
            logging.error('Table is NOT exist !("%s") '  % (table_name))
            return False
        sql = 'PRAGMA table_info("%s") ;'  % (table_name)
        logging.debug(sql)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    ###  第 3 部分：字段（列）   ################

    # 增加一个列
    def column_add(self, table_name='test_user', column_add='column_add_test text'):
        if self.teble_is_exist(table_name) == False:
            logging.debug('Table is NOT exist: %s' % table_name)
            return False
        sql_command = 'alter table %s ADD %s;' % \
                      (table_name, column_add)
        try:
            self.cursor.execute(sql_command)
            self.connect.commit()
            logging.debug('Add a column is succesful ! (%s)' %  sql_command)
        except:
            logging.error('Add a column is fail :\n ' + sql_command)
            logging.info("reference：\n"
                         "           .ColumnAdd(table_name,column_add)\n"
                         "           .ColumnAdd('col_test','col_test text')")


    #删除一个列(mysql中对应的语句是：alter table table_name drop column column_name)
    def column_drop(self):
        logging.warning('SQLite目前还不支持drop column ！ 请手工处理 ！')
        return False

    # 更改字段（列）名、属性。mysql中对应的语句是：
    # alter table table_name drop column column_name
    # alter table table_name modify column_name 新属性
    def column_change(self):
        msg = '与删除一列相同，在sqlite中alter同样无法重命名一列。'
        logging.warning(msg)
        return False


    ###  第 4 部分：表的记录（增删改查） -- 第 1 节：增   ######

    # 插入（增加）记录（批量插入法）, 用法：mydbt.value_insert(表名,字段,值)
        #  表名: 要插入的表的名字, 字符串格式
        #  字段: 字段名(注意与值对应), 字符串格式, 为空时表示所有字段，注意多个时要用括号括起来
        #   值: 要插入的值, 字符串格式, 可以多条记录同时插入
        # 示例: mydbt.value_insert('test_user',
        #       "('id','name','age')","(1,'Tom',20),
        #           (2,'Jack',21),(3,'Kite',22)")
        #   或: mydbt.value_insert('test_user','',
        #         "(1,'Tom',20),(2,'Jack',21),(3,'Kite',22)")
    def value_insert(self,
                     table_name="test_user",
                     columns="('name','age')",
                     value_insert="('Tom',20)"):
        if table_name.upper() == 'HELP':
            reference = "HELP:\n" \
                        ".value_insert(table_name,columns,values)\n" \
                        ".value_insert('test_name',\"('name','age')\",\"('Tom',20),('Kite',21)\""
            logging.info(reference)
            return reference
        if self.teble_is_exist(table_name) == False:
            logging.debug('Table is NOT exist: %s' % table_name)
            return False
        if len(str.rstrip(str.lstrip(value_insert))) == 0:
            logging.debug('无插入值数据传入')
            return False
        sql = 'insert into %s %s values %s;' % (table_name, columns, value_insert)
        logging.debug(sql)
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            logging.debug('Insert values is successful.')
            return True
        except:
            logging.error('Insert values is fail !')
            return False

    # 插入（增加）记录（逐条插入法，以用于排查数据错误）,
        #格式 ：mydbt.value_insert(表名,字段,值)
    def value_insert_onebyone(self,
                              table_name='test_user',
                              columns='',
                              value_insert=[(1, 'Tom', 20),
                                            (2, 'Kit', 23)]):
        if self.teble_is_exist(table_name) == False:
            logging.debug('Table is NOT exist: %s' % table_name)
            return False
        if len(value_insert) == 0:
            logging.debug('无插入值数据传入')
            return False
        for x in value_insert:
            v = "("
            for y in x:
                v += '"' + str(y) +'",'
            v = str.rstrip(v, ',') + ')'
            self.value_insert(table_name, columns, v)


    # 作废
    # 插入一条记录, 用法：mydbt.value_insertOne('tb1',{'name':'TomOne','age':10})
    def value_insertOne_old(self, table_name='test_user',
                            value_insert={'name':'testInserOne', 'age':1}):
        if self.teble_is_exist(table_name) == False:
            logging.debug('Table is NOT exist: %s' % table_name)
            return False
        if len(value_insert) == 0: return '无数据传入'
        col, val = '', ''
        for k in value_insert:
            col = col+k+','
            val = val+"'"+str(value_insert[k])+"'"+','
        col = col.rstrip(',')
        val = val.rstrip(',')
        sql = 'insert into %s (%s) values (%s);' % (table_name, col, val)
        logging.debug(sql)
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            logging.debug('Insert values is successful.')
        except:
            logging.debug('Insert values is fail !')

    # 作废
    #插入多条记录
    def value_insert_multi_old(self,
                              table_name='test_user',
                              InertValueList=[('name','age'),
                                              ('testvalue_insert_multi1',88),
                                              ('testvalue_insert_multi2',99)]):
        logging.debug('value_insertMulti 开始执行')
        if self.teble_is_exist(table_name) == False:
            logging.debug('Table is NOT exist: %s' % table_name)
            return False
        if len(InertValueList) == 0: return '无数据传入'
        sql_ahead = 'insert into %s ' % (table_name)

        # 处理字段元组
        col = InertValueList[0]
        if not '*' in col:       # 包含 '*' 时，表示所有字段
            sql_ahead += '('
            for x in col:
                sql_ahead = sql_ahead+str(x)+','
            sql_ahead = sql_ahead.rstrip(',') + ')'

        # 处理插入的值
        sql_ahead += ' values ('
        for n in range(1, len(InertValueList)):
            val = InertValueList[n]
            sql = sql_ahead
            for x in val:
                sql = sql + "'" + str(x) + "',"
            sql = sql.rstrip(',') + ');'
            try:
                self.cursor.execute(sql)
                self.connect.commit()
                logging.debug('插入数据成功：%s' % sql)
            except:
                logging.error('插入数据失败：\n  %s' % sql)
        logging.debug('value_insertMulti 执行完成')

    # 执行一条完整的插入命令，格式：
    #  .value_inster_execute("inster into test_user ('id','name','age') values (1,'Tom',23);")
    def value_inster_execute(self, exe_command=None):
        if exe_command == None:
            logging.error('没有参数（命令执行语句）传递进来！')
        else:
            try:
                self.cursor.execute(exe_command)
                self.connect.commit()
                logging.debug('成功执行了命令: %s' % exe_command)
            except:
                logging.error('执行命令失败: \n  %s' % exe_command)
        logging.debug('执行完成')



    ###  第 4 部分：表的记录 （增删改查） -- 第 2 节：删   #####

    # 删除记录
    def value_delete(self, table_name='test_user', condition=0):
        '''删除记录'''
        help = 'Reference: .value_delete(table_name,condition)'
        if self.teble_is_exist(table_name) == False:
            logging.error('Table is NOT exist: %s' % table_name)
            return False
        sql_command = 'delete from %s where %s ' % \
                      (table_name, condition)
        logging.debug(sql_command)
        try:
            self.cursor.execute(sql_command)
            logging.debug('Delete recorde sucessful ! ')
            return True
        except:
            msg = 'Delete recorde fail !\n %s' % (help)
            logging.error(msg)
            return True

    # 清空数据（表的初始化）
    # SQLite 不支持 truncate 进行初始化。
    # 当 SQLite 数据库中包含自增列时，会自动建立一个名为 sqlite_sequence 的表。
    # 这个表包含两个列：name 和 seq。name 记录自增列所在的表，seq 记录当前序号
    # （下一条记录的编号就是当前序号加 1）。
    # 如果要将递增数归零: DELETE FROM sqlite_sequence WHERE name = 'table_name';
    # 或者：UPDATE sqlite_sequence SET seq = 0 WHERE name = 'table_name';
    def value_truncate(self, table_name):
        if self.teble_is_exist(table_name) == False:
            logging.error('Table is NOT exist: %s' % table_name)
            return False
        try:
            sql_command1 = 'DELETE FROM %s;' % table_name
            sql_command2 = "DELETE FROM sqlite_sequence WHERE name = '%s';" % table_name
            self.cursor.execute(sql_command1)
            self.cursor.execute(sql_command2)
            self.connect.commit()
            logging.debug('Recorde truncate sucessful !'
                          '\n  %s\n  %s' % (sql_command1, sql_command2))
            return True
        except:
            logging.debug('Recorde truncate fail ! '
                          '\n  %s\n  %s' %
                          (sql_command1, sql_command2))
            return False

    ###  第 4 部分：表的记录 （增删改查） -- 第 3 节：改   ######
    def value_update(self, table_name='test_user',
                       set_new_value=None, condition=True):
        msg = 'Reference: .value_update(table_name,set_new_value,condition)'
        if self.teble_is_exist(table_name) == False:
            logging.error('Table is NOT exist: %s' % table_name)
            return False
        if set_new_value == None:
            logging.error('Recorde update fail ! \n ' + msg)
            return False
        sql_command = 'update %s set %s where %s' % \
                      (table_name, set_new_value, condition)
        try:
            self.cursor.execute(sql_command)
            logging.debug('Update recorde sucessful ! (%s)' % sql_command)
            return True
        except:
            msg = 'Update recorde fail ! (%s)' % sql_command
            logging.debug(msg)
            return False


    ###  第 4 部分：表的记录 （增删改查） -- 第 4 节：查   ######

    # 查询一个表
    def query_table(self, table_name='test_user'):
        '''查询一个表'''
        if self.teble_is_exist(table_name) == False:
            msg = ['查询错误，表不存在：%s' % table_name]
            logging.error(msg[0])
            return msg
        sql = "select * from %s " % table_name
        self.cursor.execute(sql)
        ret = self.cursor.fetchall()
        return ret

    # 执行一条完整的查询命令,格式：
    # .query_execute("select * from test_user;")
    def query_execute(self, sql_command):
        try:
            self.cursor.execute(sql_command)
            return self.cursor.fetchall()
        except:
            msg = '查询错误：%s' % sql_command
            logging.error(msg)
            return msg.split()
        else:
            msg = '查询成功：%s' % sql_command
            logging.debug(msg)


    def test(self):
        '''test'''
        self.database_connect()
        self.table_create()
        self.value_insert()
        retu = self.query_table()
        for one in retu:
            print(one)


if __name__ == "__main__":
    log_config()
    T = Dbt()
    T.test()
    print('=============')
    print(T.query_table('test_user'))
    print('---')
    T.database_disconnect()

    dbt2 = Dbt()
    dbt2.database_connect('abcd.db')
    dbt2.test()
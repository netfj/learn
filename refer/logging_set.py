#设置日志

import logging,time
def log_config(filename='runinfo.log',
               style='simplify',
               level_grade = logging.DEBUG):
    LOG_FORMAT_1 = "【%(asctime)s】\n" \
                   "路径:%(pathname)s\n" \
                   "文件:%(filename)s\n" \
                   "行号:%(lineno)d\n" \
                   "函数:%(funcName)s\n" \
                   "级别:%(levelname)s\n" \
                   "内容:%(message)s\n"
    DATE_FORMAT_1 = "%Y.%m.%d.%H:%M:%S%p"

    LOG_FORMAT_2 = "%(filename)s(%(lineno)d)%(funcName)s" \
                   "[%(levelname)s]%(message)s"
    DATE_FORMAT_2 = "%m.%d.%H:%M"

    level_grade_all = {10: '10.DEBUG', 20: '20.INFO', 30: '30.WARNING', 40: '40.ERROR', 50: '50.CRITICAL'}

    if style=='normal':
        LOG_FORMAT = LOG_FORMAT_1
        DATE_FORMAT = DATE_FORMAT_1
    else:
        LOG_FORMAT = LOG_FORMAT_2
        DATE_FORMAT = DATE_FORMAT_2
    logging.basicConfig(filename=filename,
                        level=level_grade,
                        format=LOG_FORMAT,
                        datefmt=DATE_FORMAT)
    t = "日志风格：%s  日志等级：%s  文件名：%s" % (style,level_grade_all[level_grade],filename)
    if style == 'simplify':
        t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+\
            "\n "+ t + "\n 模块  (行号)  模块或函数名  [等级]  信息内容"
    logging.info(t)

if __name__ == "__main__":
    #引用时：
    # import logging        #系统支持模块
    # import logging_set    #本模块名，如有变化随同变更
    log_config()
    def test():
        logging.debug("This is a debug log.")
        logging.info("This is a info log.")
        logging.warning("This is a warning log.")
        logging.error("This is a error log.")
        logging.critical("This is a critical log.")
    test()
    c='传递一个参数试试'
    logging.info("Test: %s",c)
    logging.error("Test: %s",c)


import logging

# 创建若干个个日志记录器，参数是起名字，一定要起，不起就是一个日志器，就是一个单例模式
# 1 创建了日志对象logger
logging_1 = logging.getLogger('log1')
# 配置：记录所有的
logging_1.setLevel(logging.DEBUG)

# 2 定义一个handles，把日志发送到文件去
fh = logging.FileHandler('text/loggingInfo.log')
ch = logging.StreamHandler()

LOGGING_INFO = "%(asctime)s -- %(filename)s -- %(levelname)s -- %(message)s"
# 3 设置格式，定义一个格式控制器
formater = logging.Formatter(LOGGING_INFO)

# 4 把格式器应用到Handlers中去，不添加，就是一个个单独的模块，不会起作用的
fh.setFormatter(formater)
ch.setFormatter(formater)

# 4.1 最关键的一步：将我们的handlers添加到logger对象中去
logging_1.addHandler(fh)
logging_1.addHandler(ch)
# fh.setLevel()     # 就算不设置也是没关系的，用前面的等级就行了

'''上述只是配置，还没有进行使用'''
try:
    1/0
except ZeroDivisionError as e :
    # 指定到哪个记录器
    logging_1.error(e)




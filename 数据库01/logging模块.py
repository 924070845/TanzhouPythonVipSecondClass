import  logging





# 对logging进行配置
# level的作用是，限制其实等级，这句话就是，INFO权限及其以上的，可以显示，比如debug就不能被显示
# 权限配置，用大写

# 看到format就想到这是一个格式化的操作
LOG_FORMAT = "%(asctime)s"

# 将日志信息保存到文件
logging.basicConfig(filename="loggingInfo.log", level=logging.INFO, format=LOG_FORMAT)
try:
    1/0
except ZeroDivisionError as e:
    logging.error(e)
    print(e)
logging.debug('救命啊')
logging.info("救命*2")
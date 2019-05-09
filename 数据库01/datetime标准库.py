import datetime
# 必须自然规范，不然报错

# 指定时间
time = datetime.time(20, 30, 59)
print(time)

# 日期
date = datetime.date(2018, 9, 7)
print(date)

# 年月日不能少，时分秒可以少
date_time = datetime.datetime(2018, 9, 6, 20, 30 ,59)
print(date_time)

# 获取当前时间
now = date_time.now()
print(now)

# 将指定时间对象转换为时间戳
time_stamp = date_time.timestamp()
print(time_stamp)

# 将时间戳转化为时间
nowtime = date_time.fromtimestamp(time_stamp)
print(nowtime)

# 将now时间转换为字符串，并按指定格式，也可之间插入值
result = now.strftime('%Y-%m-%d %H: %M')
print(result)


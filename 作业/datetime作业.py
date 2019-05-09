import datetime

birthday = input("请输入您的生日，我们将帮你计算您活了多久")

birth_day = datetime.datetime.strptime(birthday, '%Y%m%d')
print("您的生日为：{}".format(birth_day))

now = datetime.datetime.now()
print("当前时间为：{}".format(now))

# now = datetime.datetime.now()
# birth = datetime.timedelta(birth_day)
print("您活了：{}".format((now - birth_day)))

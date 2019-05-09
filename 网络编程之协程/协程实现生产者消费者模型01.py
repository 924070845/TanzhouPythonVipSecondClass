import random
import time

# 生产者函数
def Producer(cons):
    # 在协程send() 之前，必须有next阻塞，或者send(None)，并且，要写在while之前，来激活生成器
    # next(cons)
    cons.send(None)
    while True:
        # item = random.randint(0, 99)
        item = input("请输入生产者要生产的数据：")
        print("生产者：生产者生产了：{}".format(item))
        cons.send(item)     # 将生产的item发送给yield，当做yield的返回值
        time.sleep(1)

# 消费者函数
def Consumer():
    while True:
        data = yield
        print("消费者拿到了：{}".format(data))

cons = Consumer()
Producer(cons)




import greenlet
import random
import time

'''
具体的注释，在greenlet里面，这里是为了看的清晰，将注释删除的，内容一样
'''

# 生产者函数
def Producer():
    while True:
        item = random.randint(0, 99)
        print("生产者：生产者生产了：{}".format(item))
        con.switch(item)
        time.sleep(1)

# 消费者函数
def Consumer():
    while True:
        data = pro.switch()
        print("消费者拿到了：{}".format(data))

con = greenlet.greenlet(Consumer)
pro = greenlet.greenlet(Producer)

con.switch()
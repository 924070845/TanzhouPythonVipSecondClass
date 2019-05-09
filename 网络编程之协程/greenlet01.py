import greenlet
import random
import time


# 生产者函数
def Producer():
    # 在协程send() 之前，必须有next阻塞，或者send(None)，并且，要写在while之前，来激活生成器
    # next(cons)
    # cons.send(None)
    while True:
        item = random.randint(0, 99)
        # cons.send(item)     # 将生产的item发送给yield，当做yield的返回值
        print("生产者：生产者生产了：{}".format(item))
        con.switch(item)         # 切换到生产者函数
        time.sleep(1)

# 消费者函数
def Consumer():
    while True:
        # data = yield
        data = pro.switch()    # 切换到prou 协程，代替了上面的一句
        print("消费者拿到了：{}".format(data))

con = greenlet.greenlet(Consumer)      # 注意参数是函数名，不是函数的调用。
pro = greenlet.greenlet(Producer)      #这样就把一个普通的函数，变成了一个协程

# 用switch来切换使用哪个函数
con.switch()   # 运行消费者
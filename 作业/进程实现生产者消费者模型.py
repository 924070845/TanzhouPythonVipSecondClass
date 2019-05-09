import multiprocessing
import time
import random

# 生产者类（进程）
class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            data = random.randint(0, 88)
            print("生产者：向队列加入了：{}".format(data))
            self.queue.put(data)
            time.sleep(2)


# 消费者类（进程）
class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print("消费者：取出了数据：{}".format(item))
            time.sleep(2)

# 主进程
mgr = multiprocessing.Manager()

# 创建安全队列
q = mgr.Queue(5)

# 创建对象，并将队列加入其中

producer = Producer(q)
consumer = Consumer(q)

# 开启服务
producer.start()
consumer.start()

# 主进程阻塞住了，主进程不退出，程序就结束不了了。
producer.join()
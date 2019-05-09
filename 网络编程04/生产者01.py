import queue
import threading
import random
import time


# 生产者类
class Producer(threading.Thread):

    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            # 生成了一个数据，不能直接用 random，而是使用randint
            data = random.randint(0, 99)
            # 把数据放入队列
            self.queue.put(data)
            print("生产者：生产了：----{}".format(data))
            time.sleep(2)

# 消费者类
class Consumer(threading.Thread):

    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            # 把数据取出队列
            item = self.queue.get()
            print("消费者：取出了：{}".format(item))
            time.sleep(2)

# 主程序的开始


# 生成一个队列
q = queue.Queue(5)

producer = Producer(q)  # 创建了一个生产者
consumer = Consumer(q)  # 创建一个消费者

producer.start()    # 运行
consumer.start()



'''
线程的重复利用教学
'''
import time
import queue
import threading

def task_a():
    print("任务一")
    time.sleep(2)
    print("任务一完成")

def task_b(a, b, c):
    print("任务二")
    time.sleep(2)
    print("任务二完成，参数a={}，参数b={}，参数c={}".format(a, b, c))

# 生产者类（进程）
class MyThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)   # 开启守护进程，才能结束进程，要不一直等着，程序结束不了
        self.queue = queue.Queue(5)     # 将队列的创建放到类中

    # 开启线程时，自动调用run方法，不管类中的其他方法
    def run(self):
        while True:
            func, args, kwargs = self.queue.get()     # 拿到队列中的函数名
            print("拿到了：func={}, args={}, kwargs={}".format(func, args, kwargs) )
            func(*args, **kwargs)                      # 调用函数，函数拆包时的调用，第一个拆出的是元组，第二个拆出的是字典
            self.queue.task_done()                      # 让计数器 减一


    # 将对象加载进队列
    def apply_async(self, func, *args, **kwargs):
        self.queue.put((func, args, kwargs))            # 主线程调用 把函数名传入队列，函数存包时的用法

    # 自定义阻塞函数
    def join(self):
        self.queue.join()

# 主进程


# 创建对象，并将队列加入其中
thread = MyThread()
thread.start()
thread.apply_async(task_a)
thread.apply_async(task_b, (1, 2, 3), (1, 2, 3), c=(2, 3, 4))

thread.join()


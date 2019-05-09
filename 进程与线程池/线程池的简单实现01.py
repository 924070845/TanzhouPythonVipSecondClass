import threading
import time
import queue

def task_a():
    print("任务一")
    time.sleep(2)
    print("任务一完成")

def task_b(a, b, c):
    print("任务二")
    time.sleep(2)
    print("任务二完成")

# 自建线程池
# 没有继承
class MyThread_Pool:

    def __init__(self, n):
        # 创建一个队列
        self.queue = queue.Queue(5)
        # 循环创建线程
        for i in range(n):
            threading.Thread(target=self.run, daemon=True).start()


    def run(self):
        while True:
            func, args, kwargs = self.queue.get()
            print(func, args, kwargs)
            func(*args, **kwargs)
            self.queue.task_done()

    # 中文意思是：申请_异步
    # 专用来向池提交任务，将要执行的函数，丢到队列中，整个方法体包括参数，都是比较官方的形式
    def  apply_async(self, func, *args, **kwargs):
        self.queue.put((func, args, kwargs))

    def queue_join(self):
        self.queue.join()


thread = MyThread_Pool(8)       # 创建一个池（自定义的池）

thread.apply_async(task_a)
thread.apply_async(task_b, (1, 2, 3), (1, 2, 3), c=(2, 3, 4))

thread.queue_join()




import threading
import time
import queue

from multiprocessing.pool import ThreadPool     # 线程池
# from multiprocessing import Pool                # 进程池

pool = ThreadPool(4)    # 创建一个线程池，自带的池，以守护模式运行
# pool2 = Pool(4)         # 创建一个进程池


def task_a():
    print("任务一")
    time.sleep(2)
    print("任务一完成")

def task_b(a, b, c):
    print("任务二")
    time.sleep(2)
    print("任务二完成")


pool.apply_async(task_a)
pool.apply_async(task_b, args=(1, 2, 3))

pool.close()    # 先关闭线程池，关闭的意思是不能向其中提交任务了
pool.join()     # 才能join

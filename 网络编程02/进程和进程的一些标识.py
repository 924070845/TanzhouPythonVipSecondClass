import multiprocessing
from multiprocessing import Process
from threading import Thread

# 查看当前进程在哪个模块下面
print(multiprocessing.current_process())

# 使用了上面的 from 的调用后，就省略了下面这两句
# import multiprocessing
# multiprocessing.Process()

def func():
    pass


# 创建一个进程
pro = Process(target=func)

thr = Thread(target=func)



print(pro.pid)
pro.start()
print(pro.pid)
thr.start()
print(thr.ident)

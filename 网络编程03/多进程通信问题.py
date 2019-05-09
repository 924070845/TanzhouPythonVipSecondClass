import socket
import multiprocessing as mp

data = 1

def fun():
    global data     # 要修改全局变量，就要加上 global
    data = 2
    print("修改完成")

procss = mp.Process(target=fun)
procss.start()
procss.join()
print(data)
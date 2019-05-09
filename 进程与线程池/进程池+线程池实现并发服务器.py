from multiprocessing import Pool, cpu_count
from multiprocessing.pool import ThreadPool

import socket

server = socket.socket()
server.bind(('0.0.0.0', 9988))
server.listen()

def worker_thread(conn):
    while True:
        data = conn.recv(1024)
        if data :
            conn.send(data)
            print(data)
        else:
            print("没有数据了")
            conn.close()
            break

def worker_process(server):
    threadPool = ThreadPool(cpu_count()*2)      # 一般准备CPU数2倍的线程数

    while True:
        conn, addr = server.accept()    # 谁先拿到CPU资源就给谁处理
        threadPool.apply_async(worker_thread, args=(conn,))


'''
主程序
'''

'''
# 查看电脑是几核的
from multiprocessing import cpu_count
print(cpu_count())
'''

# 首先创建一个进程池，之前检测到我的CPU是2核的（在虚拟机的远程服务器，本机上是4核）
n = cpu_count()
proPppl = Pool(n)
for i in range(n):
    proPppl.apply_async(worker_process, args=(server,))

# 进程以守护模式运行，所以要退出，再join等待，不然程序会闪退
proPppl.close()
proPppl.join()













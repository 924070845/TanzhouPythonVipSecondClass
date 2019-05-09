import socket
from multiprocessing.pool import ThreadPool

server = socket.socket()
server.bind(('0.0.0.0', 9999))
server.listen()

def worker(conn):
    while True:
        data = conn.recv(1024)
        if data :
            print(data)
            conn.send(data)
        else:
            print("没有数据")
            conn.close()
            break


# 准备20个线程
threadPool = ThreadPool(20)
# 循环接收
while True:
    conn, addr = server.accept()
    threadPool.apply_async(worker, args=(conn, ))
import socket
import threading

server = socket.socket()
server.bind(('0.0.0.0', 8899))
server.listen()

# 由主线程跳转过来的，只执行的功能函数
def worker(conn):
    while True:
        data = conn.recv(1024)
        if data == b'':
            conn.close()
            break
        else:
            print(conn)
            conn.send(data)


# 主线程，只做一件事，就是看有没有人连接，接收到连接时，原来的转态是阻塞住了，
# 用锁的形式是创建一个新的线程，来处理这些个消息任务
while True:
    conn, addr = server.accept()
    print('{} 连接成功'.format(addr))
    # 线程去处理消息
    threading.Thread(target=worker, args=(conn, )).start()  #创建线程并开启



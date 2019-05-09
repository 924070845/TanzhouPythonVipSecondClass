'''
备注：
最节约资源的一个版本
'''
import gevent
from gevent import monkey
monkey.patch_socket()
# 打在socket之前，之后就没用了
# 打了这个补丁，就是将epoll注册了 socket ，下面的socket就会被epoll监控，不用自己注册了
# gevent是 epoll和协程的封装
# epoll做的事情是：检测那里的数据准备好了
import socket

# 也就是普通的服务端函数
def fun(conn):
    while True:
        data = conn.recv(1024)
        if data:
            print("收到的消息为：{}".format(data))
            conn.send(data)
        else:
            conn.close()
            break

# 将创建套接字的，放在下面
server = socket.socket()
server.bind(('0.0.0.0', 9999))
server.listen()

while True:
    conn, addr = server.accept()
    gevent.spawn(fun, conn)     # 创建了一个协程



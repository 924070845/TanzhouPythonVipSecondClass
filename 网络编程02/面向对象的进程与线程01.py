# 进程
import multiprocessing
import threading
import time
import socket

# # 面向过程
# def function():
#     print("这是子线程")
#     time.sleep(3)
#     print("子线程执行结束")
# pro = multiprocessing.Process(target=function)
# print("这是主线程")
# pro.start()

server = socket.socket()
server.bind(('0.0.0.0', 9990))
server.listen()


# 面向对象
# 想用进程的方式，就把括号里的父类换成 multiprocessing.Process
class My_Thread(threading.Thread):  # 继承 threading 类

    def __init__(self, conn):
        super().__init__()
        # 继承了父类的init 方法，在需要的地方修改就行了，相当于创建线程的那一句话
        # target参数就不用给了，他会自动触发一个run() 方法。
        # 要写的参数，写在__init__ 的括号中就行了

        self.conn =conn


    # 不需要参数
    def run(self):
        while True:
            print("这里是run() 方法")
            recv_data = self.conn.recv(1024)
            if recv_data:
                print("收到的数据{}".format(recv_data))
                self.conn.send(recv_data)
            else:
                self.conn.close()
                break


# thread = My_Thread('XXX').start()

# 开启后，自动调用run() 方法
# 不需要参数
# thread.start()

while True:
    conn, addr = server.accept()
    My_Thread(conn).start()


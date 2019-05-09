import socket
import threading

# 建立连接
server = socket.socket()
server.bind(('0.0.0.0', 9990))
server.listen()

class My_Thread(threading.Thread):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def run(self):
        while True:
            print("这里是自动执行了run() 方法")
            recv_data = self.conn.recv(1024)
            if recv_data:
                print("收到的数据为{}".format(recv_data))
                self.conn.send(recv_data)
            else:
                self.conn.close()
                break

while True:
    conn, addr = server.accept()
    My_Thread(conn).start()
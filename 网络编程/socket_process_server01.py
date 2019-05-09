import socket
import multiprocessing

server = socket.socket()
server.bind(('0.0.0.0', 9999))
server.listen()

# 建立子进程
def worker(conn):
    while True:
        data = conn.recv(1024)
        if data == b'':
            conn.close()
            break
        else:
            print(conn)
            conn.send(data)


# 建立主进程
while True:
    conn, addr = server.accept()
    print('{} 连接成功'.format(addr))
    multiprocessing.Process(target=worker, args=(conn,)).start()






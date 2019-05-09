import socket

client = socket.socket()
client.connect(('127.0.0.1', 9990))

while True:
    data = input("输入通信数据")
    client.send(data.encode())
    print('接受到的消息为{}'.format(client.recv(1024).decode()))
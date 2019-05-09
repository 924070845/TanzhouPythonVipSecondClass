import socket

client = socket.socket()
client.connect(('127.0.0.1', 8899))

while True:
    data = input("请输入数据")
    client.send(data.encode())
    print("收到的消息为：{}".format(client.recv(1024).decode()))

import socket

client = socket.socket()
client.connect(('127.0.0.1', 9999))


while True:
    data = input("请输入：")
    client.send(data.encode())
    print("接受到的值为{}".format(client.recv(1024).decode()))
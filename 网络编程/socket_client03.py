'''
我们要实现的功能是，客户端向服务端发送一个消息，
服务端可以收到，并且原封不动的返回给客户端
'''
import socket

client = socket.socket()

# 进行连接，IP是本机的意思，端口是服务端设置的端口
client.connect(('127.0.0.1', 9998))


while True:
    data = input("请输入您要说的话！")
    # 在通信时，只能传递二进制的信息，字符串时不能传递的，所以调用encode()方法，进行二进制的转码
    data = data.encode()
    # 发送信息
    client.send(data)
    print("服务端回话说：{}".format(client.recv(102).decode()))



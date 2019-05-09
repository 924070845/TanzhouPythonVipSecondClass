import socket
import threading


client = socket.socket()
client.connect(('127.0.0.1', 9999))

def recv_data():
    while True:
        data = client.recv(1024)
        print(data.decode())


username = input("输入你的用户名：")
client.send(username.encode())

thread = threading.Thread(target=recv_data, daemon=True)
thread.start()

while True:
    a = input('')
    client.send(a.encode())

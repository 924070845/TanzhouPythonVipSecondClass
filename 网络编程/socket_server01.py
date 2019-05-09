'''
我们要实现的功能是，客户端向服务端发送一个消息，
服务端可以收到，并且原封不动的返回给客户端
'''
import socket

server = socket.socket()    # 创建socket

server.bind(('0.0.0.0', 20000))     # 绑定IP地址

server.listen()     # 创建监听
# 这里的监听还可以有参数，那是解释器版本的差异，有餐数是指最多有几个用户可以连接我。
# 不加人最大，任意数连接
# 不用写的时候，你写多少都没用

print('开始监听~~~')

# 开始接受客户端的请求
# accept返回的是一个元组，conn 和 addr 是分别接受元组的两个元素
# addr 中的信息是地址和端口
# 开始执行服务端程序时，程序是阻塞在这一行的

while True:
    conn, addr = server.accept()
    print("用户 {} 已连接".format(addr))

    while True:
        data = conn.recv(1024)  # 接受用户发来的消息，这里也可以指定一个端口，用于通信。
        print('接受到的数据是：{}\t'.format(data.decode()))

        # 第二次接受到的值是 空的 所以 显示出来的是 b'', 此时就可以退出了
        if data == b'':
            conn.close()
            break
        conn.send(data)     # 发送接受到的客户端的信息

    print("跳出了while")
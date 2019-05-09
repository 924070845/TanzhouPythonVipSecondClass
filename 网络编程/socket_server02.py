'''
我们要实现的功能是，客户端向服务端发送一个消息，
服务端可以收到，并且原封不动的返回给客户端
'''
import socket
import time

'''
1:建立连接
'''
server = socket.socket()    # 创建socket
server.setblocking(False)   # 设为非阻塞
server.bind(('0.0.0.0', 8001))     # 绑定IP地址
server.listen()     # 创建监听
# 这里的监听还可以有参数，那是解释器版本的差异，有餐数是指最多有几个用户可以连接我。
# 不加人最大，任意数连接
# 不用写的时候，你写多少都没用
print('开始监听~~~')

# 开始接受客户端的请求
# accept返回的是一个元组，conn 和 addr 是分别接受元组的两个元素
# addr 中的信息是地址和端口
# 开始执行服务端程序时，程序是阻塞在这一行的



all_connection = []     # 用来保存和客户端通信的套接字

while True:
    '''
    2:处理用户的连接
    '''
    try:
        conn, addr = server.accept()
        # 只要是套接字，我们呢就把他设置为套接字
        conn.setblocking(False)
        print("用户 {} 已连接".format(addr))
        all_connection.append(conn)
    except BlockingIOError as e :
        pass

    # print('当前有 %d 个客户连接' %len(all_connection))
    # time.sleep(1.5)

    '''
    3:处理已经连接的客户端的消息
    '''
    new_li = all_connection.copy()
    for conn in new_li:
        try:
            # 这里如果不将con设置为非阻塞的话，他也会自动阻塞。
            data = conn.recv(1024)
            if data == b'':
                # 在断开连接后，就将该用户从列表中移除
                all_connection.remove(conn)
                conn.close()

            else:
                # 如果不为空，则将接受到的东西打印出来
                print("接受到的数据：{}".format(data))
                # 原封不动的返回消息
                conn.send(data)

        except BlockingIOError as e:
            pass

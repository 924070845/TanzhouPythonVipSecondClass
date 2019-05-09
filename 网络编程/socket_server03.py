import selectors    # 提供IO多路技术
import socket

server = socket.socket()
server.bind(("0.0.0.0", 9998))
server.listen()


epoll = selectors.EpollSelector()   # 生成一个spoll 选择器

# 1.2：写注册调用的函数
def funcbbb(conn):
    data = conn.recv(102)
    if data == b'':
        epoll.unregister(conn)  # 取消注册
        conn.close()
    else:
        print(data)
        conn.send(data)

# 1.1
def funcaaa(ser):
    conn, addr = ser.accept()
    print('处理了连接')
    epoll.register(conn, selectors.EVENT_READ, funcbbb)

# 1.0：调用这个参数申请注册，
# 让他帮我看着这个server（第一个参数）
epoll.register(server, selectors.EVENT_READ, funcaaa)  # 表示有数据过来了，可以读了




# 循环里面的内容才是执行工作的代码，前面都是注册、铺垫
# 让他不停的去查询，看看有没有连接
while True:

    # 在这一句会阻塞住，就算是无线循环，也不会一直跑下去
    # 每一次到这，都会停住
    events = epoll.select()  # 查询是否有请求，
    # 查询到的结果是一个列表，列表的元素是一个个元组，
    # 一组第一个值是调用的哪个函数，函数名，
    # 第二个值是套接字
    for key, mask in events:

        callback = key.data # 获取函数的名字
        sock = key.fileobj  # 获取套接字

        callback(sock)  # 函数的调用












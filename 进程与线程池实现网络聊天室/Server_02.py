from multiprocessing import Pool, cpu_count,Manager
from multiprocessing.pool import ThreadPool
import socket
from datetime import datetime

#从队列中拿出数据，发给所有连接上的客户端
def send_data(dict_proxy, queue_proxy):
    while True:
        data = queue_proxy.get()
        print(data.decode())
        for conn in dict_proxy.values():
            conn.send(data)


def worker_thread(addr, connection, dict_proxy, queue_proxy):
    while True:
        try:
            recv_data = connection.recv(1024)       # 接受客户端的消息
            if recv_data:
                time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")     # 获取当前时间，并制定格式
                data = "{addr} {time} \n \t{data}".format(addr=addr, time = time, data=recv_data.decode())
                queue_proxy.put(data.encode())      #把消息添加到到队列中
            else:
                raise Exception                     # 抛出异常
        except:
            dict_proxy.pop(addr)                    #从字典中删掉退出的客户端
            data = '{}退出'.format(addr)
            queue_proxy.put(data.encode())          #把退出消息添加到队列中
            connection.close()
            break


def login(username, conncetion, thread_pool, dict_proxy, queue_proxy ):
    dict_proxy.setdefault(username, conncetion)  # 把套接字加入字典中

    conncetion.send("恭喜你，登陆成功".encode())

    data = '{}进入房间'.format(username)
    queue_proxy.put(data.encode())  # 将用户登录消息添加到队列中
    thread_pool.apply_async(worker_thread, args=(username, conncetion, dict_proxy, queue_proxy))


def login_try(conncetion, thread_pool, dict_proxy,queue_proxy, data):
    conncetion.send(data)
    username = conncetion.recv(1024).decode()
    if username not in dict_proxy:
        login(username, conncetion, thread_pool, dict_proxy, queue_proxy)
    else:
        data = "用户名已被使用，请重新输入!".encode()
        login_try(conncetion, thread_pool, dict_proxy, queue_proxy, data)


def worker_process(server, dict_proxy, queue_proxy):
    thread_pool = ThreadPool( cpu_count()*2 )
    while True:
        conncetion, remote_address = server.accept()
        data = "".encode()
        login_try(conncetion, thread_pool, dict_proxy, queue_proxy, data)


if __name__ == '__main__':

    server = socket.socket()
    server.bind(('127.0.0.1', 9999))
    server.listen(1000)

    mgr = Manager()
    dict_proxy = mgr.dict()         #用来保存连接上来的客户端，
    queue_proxy = mgr.Queue()       #把客户端发过来的消息通过队列传递

    n = cpu_count()                 #打印当前电脑的cpu核数
    process_pool = Pool(n)
    for i in range(n-1):            #充分利用CPU，为每一个CPU分配一个进程
        process_pool.apply_async(worker_process,
                                 args=(server, dict_proxy, queue_proxy))    #把server丢到两个进程里面

    process_pool.apply_async(send_data, args=(dict_proxy, queue_proxy))     #用一个进程去收发消息

    process_pool.close()
    process_pool.join()
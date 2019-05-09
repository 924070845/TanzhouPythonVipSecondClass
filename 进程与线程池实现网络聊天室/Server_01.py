from multiprocessing import Pool, cpu_count
from multiprocessing.pool import ThreadPool
from multiprocessing import Manager
import socket
from datetime import datetime







#发消息给所有连接的客户端
def send_data(proxy_dict, proxy_queue):
    while True:
        data = proxy_queue.get()     #从队列中拿要发给客户的消息

        print('即将发送的数据：', data)
        for conn in proxy_dict.values():
            conn.send(data)



def worker_thread(conn,username, proxy_queue):
    while True:
        recv_data = conn.recv(1024)
        if recv_data:
            time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            data = "{name} {time} \n {data}".format(name=username, time=time, data = recv_data.decode())
            print(data)
            proxy_queue.put(data.encode())
        else:
            conn.close()
            data = "{}退出".format(username).encode()
            proxy_queue.put(data)
            break


def worker_process(server, proxy_dict, proxy_queue):
    thread_pool = ThreadPool( cpu_count()*2 )   #通常分配2倍CPU个数的线程
    while True:
        conn, _ = server.accept()    #生成对等套接字

        username = conn.recv(1024).decode()   #客户吧名字发过来了
        proxy_dict[username] = conn

        data = "{}登录".format(username).encode()

        proxy_queue.put(data)                #把数据丢到队列中去

        thread_pool.apply_async(worker_thread, args=(conn,username, proxy_queue))
        #异步提交


if __name__ == '__main__':

    server = socket.socket()
    server.bind(('127.0.0.1', 8888))
    server.listen(1000)

    mgr = Manager()
    proxy_dict = mgr.dict()             #保存连接的客户端， 名字当做键，对等套接字当做值
    proxy_queue = mgr.Queue()                          #消息队列

    n = cpu_count()
    process_pool = Pool(n)



    for i in range(n-1):
        process_pool.apply_async(worker_process, args=(server, proxy_dict, proxy_queue))
    process_pool.apply_async(send_data, args=(proxy_dict, proxy_queue))


    process_pool.close()
    process_pool.join()
import multiprocessing as mp


mgr = mp.Manager()      # 创建一个用于通信的空间
mgrlist = mgr.list()    # 在通信的空间中创建一个列表，和列表的使用方式一，是列表的代理

def fun(mgrlist):
    print("子进程中，mgrlist 的值为{}".format(mgrlist))
    mgrlist.append(20)
    print("子进程中，第二次的值为{}".format(mgrlist))


mgrlist.append(1)
mgrlist.append(2)

process = mp.Process(target=fun, args=(mgrlist, ))
process.start()
process.join()      # 将子进程中的内容执行完毕后，再来执行主进程


print("主线程中mgrlist的值为{}".format(mgrlist))
input()










# server = socket.socket()
# server.bind(('0.0.0.0', 8899))
# server.listen()

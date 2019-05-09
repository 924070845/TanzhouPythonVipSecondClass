import multiprocessing  # 进程模块
import time
import threading    # 线程模块

def func():
    i = 0
    while True:
        time.sleep(1)
        i += 1
        print("这是子进程————————————————————————————————————")


# 告诉这个参数，我只是要执行这个函数中的代码，只给函数名，不用加括号
# 这里函数中的func 函数名是你开的进程所要执行的函数，就两句话
process = multiprocessing.Process(target=func) # 创建一个进程
# 还要开启工作
process.start() # 运行一个进程


'''
创建一个线程，和线程用法一模一样
thread = threading.Thread(target=func, args=((1,)))
thread.start()
'''

# 这上面的代码是独立的进程，互不干扰
j = 0
while True:
    time.sleep(1)
    j += 1000000
    print("————————————————————————————————————这是主进程")


'''
主进程挂掉之后，子进程都会挂掉，而且主次进程不能认为改变
子进程出错不会影响主进程
子进程传参时必须使用元组的形式，就算是一个参数，也要括号+逗号
主子进程占那个CPU，是程序不能决定的，这是操作系统决定的
进程是操作系统分配内存空间的，而线程不会分配空间
线程是我们程序运行的实体
'''

'''
一个进程崩溃后，不会对其他进程造成影响
线程共享地址空间，一个线程非法操作搞崩后，整个进程都崩了
线程切换优于进程切换
'''

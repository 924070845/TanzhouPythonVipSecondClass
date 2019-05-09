import threading
# 创建一把锁，不创建多把锁
lock = threading.Lock()

data = 0
n = 100000

def add():
    global data
    for i in range(n):
        # 不需要都加锁，只要这一句，访问公共资源时有锁就行了。
        # 在轮询切换到我这里时，是不用切换的
        lock.acquire()
        data += 1
        # 使用完记得释放锁，一定要写的一句
        lock.release()

def sub():
    global data
    for i in range(n):
        # 推荐使用with方法，完事自动释放锁
        with lock:
            data -= 1

add_thread = threading.Thread(target=add)
sub_thread = threading.Thread(target=sub)

add_thread.start()
sub_thread.start()

add_thread.join()
sub_thread.join()

print(data)

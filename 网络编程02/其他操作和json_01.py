from threading import Thread
import time


def func():
    print("正在工作。。。")
    time.sleep(3)
    print('工作完成')

# 创建一个线程
thre = Thread(target=func)

thre.start()
thre.join()
print(thre)













#
# thre.start()
# # join这一步会推我进行阻塞，执行完子线程，才能执行主线程
# # 多个线程下，指定哪个，阻塞哪个
# thre.join()
#
# print("主线程工作做完了！")
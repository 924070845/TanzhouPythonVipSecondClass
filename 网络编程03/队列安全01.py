import queue

# 创建一个队列，什么都可以放，放函数名都可以，只要是对象
q = queue.Queue()

q.put([1,2,3,4,5])

# 队列入队操作
q.put(123)
q.put(456)
# size = q.qsize()
# print(size)

# 队列全部迭代出队操作
for i in range(q.qsize()):
    print(q.get())












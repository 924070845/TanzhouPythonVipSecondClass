import sys

def fun():
    try:
        print("第一次被调用")
        yield 1  # 遇见yield，就暂停了，如果后面有值（这里值为1），则next会返回这个1
        print("第二次被调用")
        yield
        print("第三次被调用")
        yield
    except Exception as e:
        print("执行完毕")
        print(e)
g = fun()

for i in g:
    next(g)
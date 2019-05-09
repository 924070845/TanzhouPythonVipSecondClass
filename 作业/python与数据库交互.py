import redis

conn = redis.StrictRedis(decode_responses=True)

class MyRedisList():

    # 初始化
    def __init__(self, key):
        self.conn = redis.StrictRedis(decode_responses=True)
        self.key = key

    # 添加单条数据
    def set(self, values):
        self.conn.rpush(self.key, values)

    # 添加多条数据
    def setDouble(self, *value):
        self.conn.rpush(self.key, *value)


    # 修改数据
    def updata(self, index, value):
        self.conn.lset(self.key, index=index, value=value)

    # 查询数据
    def select(self, start = 0, stop = -1, index = False):
        # 默认是全部查询，但是要添加index参数的话，也可以按索引查询
        if (type(index) == bool):
            result = self.conn.lrange(self.key, start, stop)
        else:
            result = self.conn.lindex(self.key, index)
        return result


    # 删除数据
    def delect(self):
        data = self.conn.rpop(self.key)
        return data


db = MyRedisList('lname')

# 添加数据
# for i in range(1,6):
#     db.set(i)
# *号是解包
db.setDouble(*(1,2,3,4,5,6))




# 修改数据
db.updata(2, 'xuanqing')

# 查询数据
print(db.select())
print(db.select(index=2))

# 删除数据
db.delect()
'''
rpush key value [value]  尾部添加

lrange start stop   查看数据 0 -1 就是全部

lindex key index    查看某个数据

lset key index value    修改某个数据

rpop key    删除数据

lpop key    头部数据被删除

'''





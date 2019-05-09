import pymongo

# 建立连接,要连接别人的电脑上，括号里参数host=IP
conn = pymongo.MongoClient()

# 查看MongoDB里面有哪些数据库
daabases = conn.list_database_names()
# 原来是 conn.database_names()，现在不推荐

# 选择数据库，选择的不存在时，自动创建,但是空的库不显示
db = conn['操作系统实验']

# 返回当前数据库里由哪些集合
dbs = db.collection_names()

collection = db['student']  # 选择集合，当这个集合不存在，也会自动创建一个

data = {
       'a': 1,
       'b': 2,
       'c': 3,
}
# 插入数据
collection.insert(data)
# 插入多条
collection.insert([{'name': 123},{'name': 123},{'name': 123},{'name': 123}])

result = collection.find()       # 找到的是类似于生成器的东西，用__next__()调用
# 打印
for data in result:
    print(data)




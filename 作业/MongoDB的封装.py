import pymongo

class Mongo_DB():
    def __init__(self, database_name, table_name):
        self.conn = pymongo.MongoClient()
        self.database_name = database_name
        self.table = table_name
        self.db_1 = self.conn['database_name']
        self.collection = self.db_1['table_name']

    # 添加一条文档
    def add(self, dic):
        self.collection.insert(dic)

    # 查询
    def select(self):
        return self.collection.find()

    # 修改数据
    def updata(self, dic):
        self.collection.update_many(dic)

  # 删除一条数据
    def delect(self,  dic):
        self.collection.remove(dic)
dic1 = [{'name':'xuanqing'},
       {'age':'18'},
       {'sex':'男'}]

dic2 = [{'name':'lili'},
       {'age':'16'},
       {'sex':'女'}]

# 定位到 操作系统实验 库的 student 集合
db = Mongo_DB('database_name', 'table_name')

# db.add(dic1)
# db.add(dic2)
# dic3 = [{'sex':'男'},
#         {'age':20}]
#
# db.updata(dic3)

db.delect({'age':'16'})

select_result1 = db.select()
for i in select_result1:
    print(i)




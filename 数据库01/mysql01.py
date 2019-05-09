import pymysql

db_config = {
    'db':'xuanqing2',
    'user':'root',
    'password':'qwe123',
    'charset':'utf8'    # 不是utf-8，而是utf-8
}

# 连接数据库
conn = pymysql.connect(**db_config)
# 每一次开启数据库时，都相当于给你开启了一个事务，
# 自动的，可以理解为 begin 在这里生成

# 创建游标
cur = conn.cursor()


# 执行SQL语句
# 没有提交的SQL语句，就是只能在控制台自己看看，不能写进真正的数据库
result1 = cur.execute('insert into tb1 values(4, "法丽卡")') # 返回影响了几条数据，不会讲查询结果返回
result2 = cur.execute('update tb1 set name = "娜美" where id = 1')
result3 = cur.execute('update tb1 set name = "罗宾" where id = 2')
result4 = cur.execute('update tb1 set name = "薇薇" where id = 3')
result5 = cur.execute('update tb1 set name = "卡莉法" where id = 4')
result6 = cur.execute('select * from tb1')

# 显示结果，获取真正的结果
data = cur.fetchall()

# 提交事务前，可以用代码让操作回滚
# conn.rollback()
# 可以在实现撤回操作时，吃后悔药用的
# 一定要在提交行之前写才有用
# 回滚要想好，只能全部回滚，不能回一条

# 自动提交，提交事务
conn.commit()


for i in data:
    print(i)
# 先关游标
cur.close()
# 再关连接
conn.close()


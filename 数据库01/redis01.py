import redis

conn = redis.StrictRedis(decode_responses=True) # 指定在第五号数据库，不加是定位到0号数据库
# 加上 decode_responses=True  之后，就没有了二进制的问题，就是个解码操作

result = conn.keys("*")
print(result)


# conn.delete('My_zset', 'a', 'b', 'c')
#
# conn.rename('My_zset', 'New_My_zset')

# mset 可以添加多个可以和可以values值，以字典的形式
conn.mset({'name': 1, 'name2': 2, 'name3': 3})

print(result)

print(conn.mget('name', 'name2'))


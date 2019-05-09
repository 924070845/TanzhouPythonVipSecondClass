import hashlib

# 效率低不推荐
hashlib.new('md5')

# 加减密码的数据都是二进制数据,进行进制转换：对象.encode()
hash = hashlib.md5('你好'.encode())
# 这个md5 是加密的函数，在点之后可以选择，加密方式不同，密文长度也不同

# 更新
hash.update('12'.encode()) # 在原有的数据后面，追加12，然后一起加密

# 打印加密后的值，String类型的
print(hash.hexdigest())

# 打印加密后的值，二进制类型的
print(hash.digest())

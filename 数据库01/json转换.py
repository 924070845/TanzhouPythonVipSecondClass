import json

data = {
    'a':1,
    'b':123,
    'c':{'xxx':2, 'yyy':3},
    'd':[11,22,33],
    'e':True,
    'f':False,
    'g':None
}

result = json.dumps(data)
json.dump(data, open('操作系统实验.json', 'a') )


# result2 = json.dumps(data, ensure_ascii=False)
# # print("Json数据"+result)
#
#
# dic = json.loads(result)
# print(dic)
# print(dic['d'][2])


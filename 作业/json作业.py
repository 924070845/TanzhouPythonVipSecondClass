import json

data  = {
    'name':'xuanqing',
    'age':'20',
    'fature':['高','富','帅'],
}

result = json.dump(data, open('data.json', 'a'))
dic = json.load(open('data.json', 'r'))
print(dic['fature'][2])



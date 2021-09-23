import json

# JSON 格式資料 (字串)
x = '{ "name": "Winnie Sun", "age" : "18"}'

# JSON 格式資料 -> Python Dictionary
y = json.loads(x)

# 即可使用 Python Dictionary 的方式處理資料
print(y['name'])

# CWB-FFCD9908-C3B6-429F-93AA-A50B235ADC9E
# CWB-FFCD9908-C3B6-429F-93AA-A50B235ADC9E
import json

# 取得 weather.json 內容
f = open('weather.json', encoding="utf-8")

# JSON 格式資料 -> Python Dictionary
data = json.load(f)

# 取得某縣市當前天氣資料
target = '新竹市'
res = ''
for city in data['records']['location']:
	if city['locationName'] == target:
		for element in city['weatherElement']:
			if element['elementName'] == 'Wx':
				res = element['time'][0]['parameter']['parameterName']
		break

print('目前天氣:',res)




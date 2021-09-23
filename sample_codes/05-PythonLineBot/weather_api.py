# CWB-FFCD9908-C3B6-429F-93AA-A50B235ADC9E
import json
import requests

# 透過中央氣象局 API 取得天氣資料
api_url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-FFCD9908-C3B6-429F-93AA-A50B235ADC9E&sort=time'
resp = requests.get(api_url)

# 如果擷取資料成功再做解析
if resp.status_code == 200:
	# JSON 格式資料 -> Python Dictionary (兩種方法，擇一使用)
	#data = resp.json()
	data = json.loads(resp.content)

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
else:
	print(resp.status_code)




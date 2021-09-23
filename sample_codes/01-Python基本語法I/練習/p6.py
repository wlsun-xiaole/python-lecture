# 這是一個可以重複執行的閏平年判斷程式
times = input('請問需要查詢幾次?')
times = int(times)

for i in range(times):
  year = input('請輸入一個西元年份: ')
  year = int(year)

  # 判斷閏平年
  if (year % 400 == 0) or (year%4 == 0 and year%100 != 0):
      print('這是西元', year, '這是一個閏年!')
  else:
      print('這是西元', year, '這是一個平年!')
  
print('程式結束囉!')


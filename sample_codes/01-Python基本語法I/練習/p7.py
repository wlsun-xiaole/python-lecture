# 這是一個可以重複執行的閏平年判斷程式
years = [ 2000, 2001, 2004, 2100, 1900 ]
for year in years:
  # 判斷閏平年
  if (year % 400 == 0) or (year%4 == 0 and year%100 != 0):
      print('這是西元', year, '這是一個閏年!')
  else:
      print('這是西元', year, '這是一個平年!')
  
print('程式結束囉!')

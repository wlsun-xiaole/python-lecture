# 這是一個閏平年判斷程式
year = input('請輸入一個民國年份: ')
year = int(year)

# 民國年轉西元年
year += 1911

# 判斷閏平年
if (year % 400 == 0) or (year%4 == 0 and year%100 != 0):
    print('這是西元', year, '這是一個閏年!')
else:
    print('這是西元', year, '這是一個平年!')

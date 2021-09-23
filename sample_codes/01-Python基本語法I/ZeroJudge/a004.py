while True:
  try:
    # 主程式 開始
    year = int(input())
    if (year % 400 == 0) or (year%4 == 0 and year%100 != 0):
        print('閏年')
    else:
        print('平年')
    # 主程式 結束
  except:
    break
  
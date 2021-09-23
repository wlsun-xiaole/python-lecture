# 這是一支計算BMI的程式
name = input("請問您的名字是? ")
weight = input("請問您的體重是(公斤)? ")
weight = int(weight)
height = input("請問您的身高是(公尺)? ")
height = float(height)
BMI = weight / ( height * height)  # 計算BMI
print(name, '的BMI指數是 ', BMI) # 輸出BMI計算結果

# 判斷體重範圍
if BMI < 18.5:
  print('評估結果: 過輕')
elif BMI < 24:
  print('評估結果: 正常')
elif BMI < 27:
  print('評估結果: 過重')
elif BMI < 30:
  print('評估結果: 輕度肥胖')
elif BMI < 35:
  print('評估結果: 中度肥胖')
else:
  print('評估結果: 重度肥胖')
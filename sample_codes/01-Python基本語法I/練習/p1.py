# 這是一支計算BMI的程式
name = input("請問您的名字是? ")
weight = input("請問您的體重是(公斤)? ")
weight = int(weight)
height = input("請問您的身高是(公尺)? ")
height = float(height)
BMI = weight / ( height * height)  # 計算BMI
print(name, '的BMI指數是 ', BMI) # 輸出BMI到螢幕上

# 這是一支評估體脂率的程式
sex = input("請問您的性別是?(男/女) ")
BFP = input("請問您的體脂率是(%)? ")
BFP = float(BFP)

# 判斷體脂率範圍
if sex == '男':
  if BFP < 17:
    print('評估結果: 過低')
  elif BFP < 23:
    print('評估結果: 正常')
  else:
    print('評估結果: 過高')
else:
  if BFP < 20:
    print('評估結果: 過低')
  elif BFP < 27:
    print('評估結果: 正常')
  else:
    print('評估結果: 過高')
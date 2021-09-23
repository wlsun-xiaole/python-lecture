# 這支程式使用break
times = input("請問要輸出幾次? ")
times = int(times)
i = 0
while i < times :
    i = i + 1
    if i == 4:
        break
    print('這是第', i, '次')
print('程式結束了!')

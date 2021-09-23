# 導入 random 模組
import random

# 設定 seed 值
random.seed(10)

# 打亂序列 shuffle()
mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(mylist)
print(mylist)
random.shuffle(mylist)
print(mylist)

# 隨機產生一個範圍內的整數
print(random.randint(5,10))

# 隨機產生一個 0.0 ~ 0.1 內的浮點數
print(random.random())

# 有預設參數值
def my_function(**nums):
    print(nums["a"])
# 可傳入任意數量的具名參數
my_function(a = 10, b = 11)
my_function(a = 10)

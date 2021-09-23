st, ed = input().split()
flag = True
for i in range(int(st),int(ed)):
    L = len(str(i))
    c = 0
    for s in str(i):
        c += pow(int(s),L)
    if i == c:
        flag = False
        print(i, end=' ')
if flag:
    print('none')
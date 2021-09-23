a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
res = b*b-4*a*c
if  res == 0:
  root = -b / (2*a)
  print('Two same roots x=%d'%root)
elif res < 0:
  root = -b / (2*a)
  print('No real root')
else:
  root1 = int((-b + res**0.5) / (2*a))
  root2 = int((-b - res**0.5) / (2*a))
  print('Two different roots x1=%d , x2=%d'%(root1,root2))
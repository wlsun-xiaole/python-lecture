while True:
  try:
    s = input()
    res = ''
    for x in s:
      if not x.isalpha():
        res += ' '
      else:
        res += x
    print(len(res.split()))
  except:
    break

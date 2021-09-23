# ZeroJudge a053
num = int(input())
score = 0
if num < 10:
  score += num*6
elif num < 20:
  score += 10*6 + (num-10)*2
elif num < 40:
  score += 10*6 + 10*2 + (num-20)
else:
  score = 100
print(score)


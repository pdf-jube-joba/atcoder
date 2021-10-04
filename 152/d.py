def rec(X) :
  if X <= 0 :
    return 0
  elif X == 1 :
    return 1
  else :
    return 1 + 2 * rec(X // 2)

H = int(input())
print(rec(H))
def main(a , b , c) :
  if a == b :
    return c
  elif b == c :
    return a
  elif c == a:
    return b
  else :
    return 0

a , b , c = list(map(int , input().split()))
print(main(a , b , c))
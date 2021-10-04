def main(A , B):
  c = B - A + 1
  if c <= 0 :
    return 0
  else :
    return c

A , B = list(map(int , input().split()))
print(main(A , B))
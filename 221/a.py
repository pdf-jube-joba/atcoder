def main(A,B):
  return 32 ** (A - B)

A , B = list(map(int , input().split()))
print(main(A,B))
def main(N , C):
  max_C = max(C)
  D1 = [[0] * N] * max_C
  D2 = [[0] * N] * max_C

  for i in range(N) :
    for j in range(C[i]) :
      pass


N = int(input())
C = list(map(int , input().split()))
print(main(N , C))
def main(N , A) :
  A.sort()
  for i in range(N - 1) :
    if A[i] == A[i + 1] :
      return "NO"
  return "YES"

N = int(input())
A = list(map(int , input().split()))
print(main(N , A))
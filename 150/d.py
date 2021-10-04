import math

def gcd(x , y):
  if x > y :
    return gcd(y , x)
  if x == 0 :
    return y
  return gcd(y % x, x)
  
def lcm(x , y):
  return (x * y) // gcd(x , y)

def main(N , A , M) :
  A_ = [A[i] // 2 for i in range(N)]
  minA = 1
  for i in range(N) :
    minA = lcm(minA , A_[i])

  for i in range(N) :
    if (minA // A_[i]) % 2 == 0 :
      return 0

  return math.floor(((M / minA) - 1) / 2) + 1

N , M = list(map(int , input().split()))
A = list(map(int , input().split()))
print(main(N , A , M))
def expected(P) :
  return (P + 1) / 2

def main(N , K , p) :
  sum = 0
  for i in range(K) :
    sum += expected(p[i])
  maximum = sum

  for i in range(N - K) :
    sum = sum - expected(p[i]) + expected(p[i + K])
    maximum = max(sum , maximum)

  return maximum

N , K = list(map(int , input().split()))
p = list(map(int , input().split()))
print(main(N , K , p))
def operation(N) :
  if N % 200 == 0 :
    return N // 200
  else :
    return N * 1000 + 200

def main(N , K) :
  if K == 0 :
    return N
  else :
    return main(operation(N) , K - 1)

N , K = list(map(int , input().split()))
print(main(N , K))
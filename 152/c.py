def main(N , K , H):
  H.sort()

  if N <= K :
    return 0
  
  sum = 0
  for i in range(N - K):
    sum += H[i]
  
  return sum

N , K = list(map(int , input().split()))
H = list(map(int , input().split()))
print(main(N , K , H))
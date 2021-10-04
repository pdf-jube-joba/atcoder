def main(N , K , M , A) :
  sum_A = sum(A)
  min = N * M - sum_A
  if K < min :
    return -1
  elif min <= 0:
    return 0
  else :
    return min

N , K , M = list(map(int , input().split()))
A = list(map(int , input().split()))
print(main(N , K , M , A))
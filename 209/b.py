def main(N , X , A) :
  sum = 0
  for i in range(N) :
    if (i + 1) % 2 == 0 :
      sum += A[i] - 1
    else :
      sum += A[i]

  if sum <= X :
    return "Yes"
  else :
    return "No"

N , X = list(map(int , input().split()))
A = list(map(int , input().split()))
print(main(N , X , A))
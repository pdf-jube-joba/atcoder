def main(H , N , A):
  sum = 0
  for i in range(N) :
    sum += A[i]

  if H <= sum :
    return "Yes"
  else :
    return "No"

H , N = list(map(int , input().split()))
A = list(map(int , input().split()))
print(main(H , N , A))
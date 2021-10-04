def second(N , T):
  if T[0] < T[1] :
    first = 1
    second = 0
  else :
    first = 0
    second = 1

  for i in range(2 , N) :
    if T[first] < T[i] :
      second = first
      first = i
    elif T[second] < T[i] :
      second = i

  return second

N = int(input())
S = [0] * N
T = [0] * N
for i in range(N) :
  in1 = input().split()
  S[i] = in1[0]
  T[i] = int(in1[1])
print(S[second(N , T)])
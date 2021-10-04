def main(N , M , p , S) :
  clear = [False] * N
  WA = [0] * N

  for i in range(M) :
    problem = p[i] - 1
    if not(clear[problem]) :
      if S[i] == "WA" :
        WA[problem] += 1
      else :
        clear[problem] = True

  total_clear = 0
  total_WA = 0

  for i in range(N) :
    if clear[i] :
      total_clear += 1
      total_WA += WA[i]

  return total_clear , total_WA

N , M = list(map(int , input().split()))
p = [0] * M
S = [0] * M
for i in range(M) :
  in1 = input().split()
  p[i] = int(in1[0])
  S[i] = in1[1]

result = main(N , M , p , S)
print(result[0] , result[1])
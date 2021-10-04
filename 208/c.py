in1 = list(map(int , input().split()))
in2 = list(map(int , input().split()))

N = in1[0]
K = in1[1]
a = in2

base = K // N
rem = K % N

ans = [base] * N

X = []
for i in range(N) :
  X.append((a[i] , i))

X.sort(key=lambda x: x[0])

for i in range(rem) :
  j = X[i][1]
  ans[j] += 1

for i in range(N) :
  print(ans[i]) 
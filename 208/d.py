def cost_sum(A , B) :
  if A[1] and B[1] :
    return (A[0] + B[0] , True)
  else :
    return (0 , False)

def cost_min_of_2(A , B):
  if A[1] :
    if B[1] :
      return (min(A[0] , B[0]) , True)
    else :
      return A
  else :
    return B

def cost_alt_sum(s , A) :
  if A[1] :
    return s + A[0]
  else :
    return s



def main(N , M , A , B , C) :

  now_min_cost = [[(0 , i == j) for i in range(N + 1)] for j in range(N + 1)]
  for path in range(M) :
    p_to = A[path]
    p_from = B[path]
    p_cost = C[path]
    now_min_cost[p_to][p_from] = (p_cost , True)

  sum = 0

  for k in range(1 , N + 1) :
    for s in range(1 , N + 1) :
      for t in range(1 , N + 1) :
        now_min_cost[s][t] = \
          cost_min_of_2(now_min_cost[s][t] , cost_sum(now_min_cost[s][k] , now_min_cost[k][t]))
        sum = cost_alt_sum(sum , now_min_cost[s][t])
  
  return sum

in1 = list(map(int , input().split()))
N = in1[0]
M = in1[1]

A = [0] * M
B = [0] * M 
C = [0] * M

for i in range(M) :
  in2 = list(map(int , input().split()))
  A[i] = in2[0]
  B[i] = in2[1]
  C[i] = in2[2]

print(main(N , M , A , B , C))
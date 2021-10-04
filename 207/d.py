def point_minus(A , B) :
  return (A[0] - B[0] , A[1] - B[0])

def able_rot_to(A , B) :
  return (A[0] ^ 2 + A[1] ^ 2) == (B[0] ^ 2 + B[1] ^ 2)

def complex_rot_of(A , B) :
  pass

def main(N , S , T) :

  if N == 0 :
    return "Yes"

  S_ = [(0 , 0)] * N
  for i in range(N) :
    S_[i] = point_minus(S[i] , S[0])
  
  for i in range(N) :
    T_ = [(0 , 0)] * N
    for j in range(N) :
      T_[j] = point_minus(T[j] , T[i])

    for j in range(N) :
      pass


### N = int(input())
### P = [(0 , 0)] * N
### Q = [(0 , 0)] * N
### 
### for i in range(N) :
###   in1 = list(map(int , input().split()))
###   P[i] = (in1[0] , in1[1])
### for i in range(N) :
###   in2 = list(map(int , input().split()))
###   Q[i] = (in2[0] , in2[1])

N = 3
S = [(0 , 0) , (0 , 1) , (1 , 0)]
T = [(2 , 0) , (3 , 0) , (3 , 1)]

main(N , S , T)
def main(A1 , A2 , A3) :
  b : bool
  
  if A1 <= A2 and A2 <= A3 :
    b = (A2 - A1 == A3 - A2)
  elif A1 <= A3 and A3 <= A2 :
    b = (A3 - A1 == A2 - A1)
  elif A2 <= A1 and A1 <= A3 :
    b = (A1 - A2 == A3 - A1)
  elif A2 <= A3 and A3 <= A1 :
    b = (A3 - A2 == A1 - A3)
  elif A3 <= A1 and A1 <= A2 :
    b = (A1 - A3 == A2 - A1)
  elif A3 <= A2 and A2 <= A1 :
    b = (A2 - A3 == A1 - A1)
  
  if b :
    return("Yes")
  else :
    return("No")

A = list(map(int , input().split()))
A1 = A[0]
A2 = A[1]
A3 = A[2]
print(main(A1 , A2 , A3))
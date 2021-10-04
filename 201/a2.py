def main(A1 , A2 , A3):
  if 2 * A1 == A2 + A3 :
    return "Yes"
  elif 2 * A2 == A1 + A3 :
    return "Yes"
  elif 2 * A3 == A1 + A2 :
    return "Yes"
  else :
    return "No"

A = list(map(int , input().split()))
A1 = A[0]
A2 = A[1]
A3 = A[2]
print(main(A1 , A2 , A3))
def main(A,B):
  if A == B :
    return "Yes"
  N = len(A)
  X = B
  for i in range(N - 1) :
    if (not(A[i] == B[i]) and not(A[i + 1] == B[i + 1])) :
      X = B[0 : i] + B[i + 1] + B[i] + B[i + 2:]
      break
  if A == X :
    return "Yes"
  else :
    return "No"

S = input()
T = input()
print(main(S,T))
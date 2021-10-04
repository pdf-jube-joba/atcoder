def main(A1 , A2 , A3):
  A_max = max(A1 , A2 , A3)
  A_min = min(A1 , A2 , A3)
  A_ave = (A1 + A2 + A3)

  return 3 * (A_max + A_min) == 2 * A_ave

# A3 - A2 == A2 - A1
# <=> A1 + A3 = 2 * A2
# <=> 3 * (A1 + A3) = 2 * (A1 + A2 + A3)

A = list(map(int , input().split()))
A1 = A[0]
A2 = A[1]
A3 = A[2]
print(main(A1 , A2 , A3))
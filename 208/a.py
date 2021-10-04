in1 = list(map(int , input().split()))
A = in1[0]
B = in1[1]

if B <= 6 * A and A <= B:
  print("Yes")
else :
  print("No")
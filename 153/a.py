def main(S , A , T , B , U) :
  if S == U :
    return (A - 1 , B)
  else :
    return (A , B - 1)

S , T = input().split()
A , B = list(map(int , input().split()))
U = input()

result = main(S , A , T , B , U)
print(result[0] , result[1])
def main(H , A) :
  if H % A == 0 :
    return H // A
  else :
    return H // A + 1

H , A = list(map(int , input().split()))
print(main(H , A))
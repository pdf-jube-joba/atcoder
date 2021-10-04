def main(S1 , S2 , S3 , T):
  ret = ""
  for t in T :
    if t == "1" :
      ret = ret + S1
    if t == "2" :
      ret = ret + S2
    if t == "3" :
      ret = ret + S3
  return ret

S1 = input()
S2 = input()
S3 = input()
T = input()
print(main(S1 , S2 , S3 , T))
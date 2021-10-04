def rec(S1 , S2 , S3 , T) :
  if len(T) == 0 :
    return ""

  T_head = T[0]
  T_tail = T[1 : len(T)]
  if T_head == "1" :
    return S1 + rec(S1 , S2 , S3 , T_tail)
  if T_head == "2" :
    return S2 + rec(S1 , S2 , S3 , T_tail)
  if T_head == "3" :
    return S3 + rec(S1 , S2 , S3 , T_tail)

S1 = input()
S2 = input()
S3 = input()
T = input()
print(rec(S1 , S2 , S3 , T))
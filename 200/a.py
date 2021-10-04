def main(N) :
  if N % 100 == 0:
    return N // 100
  else :
    return N // 100 + 1

N = int(input())
print(main(N))
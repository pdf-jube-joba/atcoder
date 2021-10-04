def main(N , S) :
  count = 0
  for i in range(N - 2) :
    if S[i : i + 3] == "ABC" :
      count += 1
  
  return count

N = int(input())
S = input()
print(main(N , S))
import itertools

def main(N , P , Q):
  all = list(itertools.permutations(range(1 , N + 1)))
  index_P = all.index(tuple(P))
  index_Q = all.index(tuple(Q))
  return abs(index_P - index_Q)

N = int(input())
P = list(map(int , input().split()))
Q = list(map(int , input().split()))

print(main(N , P , Q))
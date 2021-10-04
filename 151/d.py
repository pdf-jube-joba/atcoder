import queue

def valid(H , W , X) :
  return (0 <= X[0]) and (X[0] < H) \
  and (0 <= X[1]) and (X[1] < W)

def max_from(H , W , S , I , J) :
  if S[I][J] == "#" :
    return 0
  
  count = 0
  state = [["uncomputed" for i in range(W) ] for j in range(H) ]
  Dxy = [(0 , 1) , (0 , -1) , (1 , 0) , (-1 , 0)]
  q = queue.Queue()

  q.put([0 , (I , J)])

  while not q.empty() :
    s = q.get()
    dist = s[0]
    now = s[1]
    state[now[0]][now[1]] = "computed"
    count = max(dist , count)

    for dxy in Dxy :
      candi = (now[0] + dxy[0] , now[1] + dxy[1])
      if valid(H , W , candi) and S[candi[0]][candi[1]] == "." \
      and (state[candi[0]][candi[1]] == "uncomputed") :
        q.put([dist + 1 , candi])
        state[candi[0]][candi[1]] = "queued"

  return count

def main(H , W , S) :
  max_dist = 0
  for i in range(H) :
    for j in range(W) :
      max_dist = max(max_dist , max_from(H , W , S , i , j))

  return max_dist


H , W = list(map(int , input().split()))
S = [["." for i in range(W)] for j in range(H)]
for i in range(H) :
  S[i] = input()

print(main(H , W , S))
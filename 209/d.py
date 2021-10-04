def main(N , Q , a , b , c , d):
  

N , Q = list(map(int , input().split()))
a = [0] * N
b = [0] * N
c = [0] * N
d = [0] * N
for i in range(N) :
  a[i] , b[i] = list(map(int , input().split()))
for i in range(N) :
  c[i] , d[i] = list(map(int , input().split()))
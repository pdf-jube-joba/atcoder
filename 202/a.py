def main(a,b,c):
  return (7 - a) + (7 - b) + (7 - c)

in1 = list(map(int , input().split()))
a = in1[0]
b = in1[1]
c = in1[2]
print(main(a , b , c))
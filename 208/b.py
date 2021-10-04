import math
P = int(input())

remaine = P
count = 0

for i in range(10) :
  coin = math.factorial(10 - i)
  while(coin <= remaine) :
    count = count + 1
    remaine = remaine - coin

print(count)
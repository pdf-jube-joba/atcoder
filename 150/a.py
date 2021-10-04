def main(K , X) :
  if X <= 500 * K :
    return "Yes"
  else :
    return "No"

K , X = list(map(int , input().split()))
print(main(K , X))
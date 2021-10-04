def main(X):
  if 0 <= X and X < 40 :
    return 40 - X
  if 40 <= X and X < 70 :
    return 70 - X
  if 70 <= X and X < 90 :
    return 90 - X
  return "expert"

X = int(input())
print(main(X))
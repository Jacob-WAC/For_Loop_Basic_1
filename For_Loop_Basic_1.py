for x in range(151):
  print(x)

for x in range(5,1001):
  if x % 5 == 0:
    print(x)

for x in range(1,101):
  if x % 10 == 0:
    print("coding dojo")
  elif x % 5 == 0:
    print("coding")
  else:
    print(x)

temp = 0
for x in range(500001):
  if x % 2 != 0:
    temp += x
print(temp)

for x in range(2018,0,-4):
  print(x)

lowNum = 2 
highNum = 9 
mult = 3

for x in range(lowNum,highNum + 1):
  if x % mult == 0:
    print(x)
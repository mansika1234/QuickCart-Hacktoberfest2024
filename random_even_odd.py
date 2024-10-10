import random
def randomOddNumber(a,b):
  a = a // 2
  b = b // 2 - 1
  number = random.randint(a,b)
  number = (number * 2) + 1
  return number
  
oddNumber = randomOddNumber(0,100) 
print(oddNumber)

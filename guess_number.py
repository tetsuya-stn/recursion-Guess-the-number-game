import random
import sys

min = int(input('Input minimum number: '))
max = int(input('Input maximum number: '))

if max <= min:
  print('maximum number has to be greater than minimum number')
  sys.exit()

answer = random.randint(min, max)

for i in range(min):
  estimate = int(input('Estimate random number: '))

  if estimate == answer:
    print('Correct! Congratulations!')
    sys.exit()

print('Better luck next time!')

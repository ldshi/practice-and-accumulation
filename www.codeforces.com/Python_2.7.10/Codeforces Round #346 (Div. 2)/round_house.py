#
## python --version -> Python 2.7.10
#

import math

def move(max, current, direction):
  if direction > 0:
    if current < max:
      return current + 1
    elif current == max:
      return 1
  else:
    if current == 1:
      return max
    elif current > 1:
      return current - 1

inputs = raw_input().strip().split(' ')
total = int(inputs[0])
start = int(inputs[1])
direction = int(inputs[2])

counter = math.fabs(direction)

while counter > 0:
  start = move(total, start, direction)

  counter -= 1

print start



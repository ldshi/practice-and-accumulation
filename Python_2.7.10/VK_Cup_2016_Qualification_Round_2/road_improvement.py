#
## python --version -> Python 2.7.10
#

import sys

amount = 0

accumulation = []

def accumulator(road_number, road):
  if len(accumulation) == 0:
    accumulation.append([[road_number], road])
    return

  for item in accumulation:
    if road[0] not in item[1] and road[1] not in item[1]:
      item[0].append(road_number)
      item[1] = item[1] + road
      return

  accumulation.append([[road_number], road])


amount = int(raw_input())

tmp = 1
while tmp < amount:
  accumulator(tmp, raw_input().strip().split(' '))
  tmp += 1



print len(accumulation)

for item in accumulation:
  sys.stdout.write(str(len(item[0])) + ' ' + ' '.join(str(e) for e in item[0]) + '\n')



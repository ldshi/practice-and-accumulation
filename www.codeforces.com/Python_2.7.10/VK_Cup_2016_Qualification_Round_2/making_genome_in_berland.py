#
## python --version -> Python 2.7.10
#

import difflib, re

amount = 0

records = []

def appender(item):
  if len(records) == 0:
    records.append(item)
    return

  idx = len(records) - 1
  while idx >= 0:
    if item in records[idx]:
      return
    elif records[idx] in item:
      records[idx] = item
      return

    if idx == 0:
      records.append(item)

    idx -= 1

def reducer(res, item):
  if item in res:
    return res

  sm = difflib.SequenceMatcher(None, res, item)
  overlap = sm.find_longest_match(0, len(res), 0, len(item))

  tmp_res = ''.join(res.split())
  if item in tmp_res:
    if overlap.b == 0:
      res = res[0 : overlap.a + overlap.size] + res[overlap.a + overlap.size + 1 : len(res)]
    else:
      res = res[0 : overlap.a - overlap.b] + res[overlap.a - overlap.b + 1 : len(res)]
    return res

  if overlap.size == 0:
    res = res + item + ' '
  else:
    if overlap.b == 0:
      if res[overlap.a + overlap.size] == ' ':
        res = res[0 : overlap.a] + item[0 : len(item)] + ' ' + res[overlap.a + overlap.size + 1 : len(res)]
      else:
        res = res + item + ' '
    elif overlap.size == len(item) - overlap.b:
      if overlap.a - 1 > 0:
        res = res[0 : overlap.a] + item[0 : overlap.b] + res[overlap.a : len(res)]
      else:
        res = item[0 : overlap.b] + res[overlap.a : len(res)]
    else:
      res = res + item + ' '

  return res



amount = int(raw_input())

while amount > 0:
  appender(raw_input().strip())
  amount -= 1



records.sort(key = lambda e: -len(e))

tmp_result = ' '.join(records)

while True:
  result_0 = ''

  result_0_arr = tmp_result.split(' ')

  for item in result_0_arr:
    if item == '':
      continue
    else:
      result_0 = tmp_result = reducer(result_0, item)

  result_1 = ''

  result_1_arr = tmp_result.split(' ')

  for item in result_1_arr:
    if item == '':
      continue
    else:
      result_1 = tmp_result = reducer(result_1, item)

  if (len(result_0) == len(result_1)):
    break



print ''.join(result_0.split())



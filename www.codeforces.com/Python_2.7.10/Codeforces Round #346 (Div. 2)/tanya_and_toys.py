#
## python --version -> Python 2.7.10
#

first_line = raw_input().strip().split(' ')

second_line = raw_input().strip().split(' ')

controller = int(first_line[1])

accumulation = []
accumulation_val = 0
tmp = 1
while accumulation_val < controller:
  if str(tmp) not in second_line:
    if accumulation_val + tmp <= controller:
      accumulation.append(str(tmp))
      accumulation_val += tmp
    else:
      break

  tmp += 1

print len(accumulation)
print ' '.join(accumulation)



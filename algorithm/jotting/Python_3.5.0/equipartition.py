#
## There are three cans, all don't have scale, and the capacity respectively are 12 liter, 8 liter, 5 liter,
##   at initial: the 12 liter one with full liquid, the others two are empty
#
## Find a solution to get two cans of 6 liter liquid.
#

def equipartition():

  def gcd(a, b):
    if str(a).isdigit() and str(b).isdigit():
      if b == 0:
        return a
      else:
        return gcd(b, a % b)

  def has_solution(a, b, c):
    if str(a).isdigit() and str(b).isdigit() and str(c).isdigit():
      if c % gcd(a, b) == 0:
        return True
      else:
        return False

  #
  ## Five rules:
  ##   1. 12L -> 8L
  ##   2. 8L  -> 5L
  ##   3. 5L  -> 12L
  ##   4. Only when the 5L can is full then can execute the rule 3
  ##   5. Only when the 5L can is empty then can execute the rule 2
  #
  if has_solution(8, 5, 6):
    status = [(12, 0, 0)]

    print('12L 8L 5L')

    while True:
      print('%3d %2d %2d' % (status[-1][0], status[-1][1], status[-1][2]))
      if status[-1].count(6) == 2:
        return
      elif status[-1].count(6) == 1:
        status.append((6, 6, 0))
      elif status[-1][2] == 0 and status[-1][1] > 0:
        status.append((status[-1][0], 0 if status[-1][1] <= 5 else status[-1][1] - 5, 5 if status[-1][1] >= 5 else status[-1][1]))
      else:
        idx = status[-1].index(max(status[-1]))
        if idx == 0:
          status.append((0 if 8 - status[-1][1] >= status[-1][0] else status[-1][0] - (8 - status[-1][1]), 8 if status[-1][0] >= 8 - status[-1][1] else status[-1][1] + status[-1][0], status[-1][2]))
        elif idx == 1:
          status.append((status[-1][0], 0 if 5 - status[-1][2] >= status[-1][1] else status[-1][1] - (5 - status[-1][2]), 5 if status[-1][1] >= 5 - status[-1][2] else status[-1][2] + status[-1][1]))
        else:
          # Actually this check is unnecessary
          if status[-1][2] == 5:
            status.append((12 if status[-1][0] >= 7 else status[-1][0] + 5, status[-1][1], 0 if status[-1][0] <= 7 else 5 - (12 - status[-1][0])))

  else:
    print('No solution')

equipartition()



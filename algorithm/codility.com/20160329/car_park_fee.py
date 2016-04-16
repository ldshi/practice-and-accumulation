#
## python --version -> Python 2.7.10
#

fee_entr = 2
fee_1st_h = 3
fee_after_2nd_per_h = 4

def solution(E, L):

  e_arr = E.split(':')
  l_arr = L.split(':')

  in_min = (int(l_arr[0]) - int(e_arr[0])) * 60 - int(e_arr[1]) + int(l_arr[1])

  if in_min <= 60:
    print fee_entr + fee_1st_h
  else:
    if in_min % 60 == 0:
      print fee_entr + fee_1st_h + (in_min / 60 - 1) * fee_after_2nd_per_h
    else:
      print fee_entr + fee_1st_h + (int(in_min / 60)) * fee_after_2nd_per_h



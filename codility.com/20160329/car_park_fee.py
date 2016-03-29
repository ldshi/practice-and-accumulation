fee_entrance = 2
fee_1st_hour = 3
fee_per_after_2nd_hour = 4

def solution(E, L):

  e_arr = E.split(':')
  l_arr = L.split(':')

  by_min = (int(l_arr[0]) - int(e_arr[0])) * 60 - int(e_arr[1]) + int(l_arr[1])

  if by_min <= 60:
    return fee_entrance + fee_1st_hour 
  else:
    if by_min % 60 == 0:
      return fee_entrance + fee_1st_hour + (by_min / 60 - 1) * fee_per_after_2nd_hour
    else:
      return fee_entrance + fee_1st_hour + (int(by_min / 60)) * fee_per_after_2nd_hour



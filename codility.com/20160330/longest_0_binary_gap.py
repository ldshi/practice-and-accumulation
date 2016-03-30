def solution(N):
  str = '{0:b}'.format(N)
  
  counter = prev_counter = 0
  for c in str:
    if c is '0':
      counter += 1
    else:
      if prev_counter == 0 or counter > prev_counter:
        prev_counter = counter
      counter = 0

  return prev_counter if prev_counter > counter else counter



def solution(A, B):
  tmp = '{0:b}'.format(A * B)

  return list(tmp).count('1')



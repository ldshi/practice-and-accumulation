def solution(A):

  begin = end = 0

  accumulation = []

  res = 0

  while begin < len(A) - 2:
    end = begin + 1
    tmp = A[end] - A[begin]

    while end < len(A) and A[end] - A[end - 1] == tmp:
      end += 1

    if end - begin >= 3:
      accumulation.append([begin, end - 1])

      begin = end - 1
    else:
      begin += 1

  for item in accumulation:
    tmp = item[1] - item[0] + 1 - 2
    res += tmp * (tmp + 1) / 2

  return res



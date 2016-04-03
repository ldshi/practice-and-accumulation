def solution(A):

  exchange_0 = exchange_1 = pos = -1

  idx = 1
  while idx < len(A):
    if A[idx] < A[idx - 1]:
      if exchange_0 == -1:
        exchange_0 = A[idx - 1]
        exchange_1 = A[idx]
      else:
        return False

    if exchange_0 > 0:
      if A[idx] > exchange_0:
        if A[idx - 1] > exchange_1:
          return False
        else:
          pos = idx - 1

    idx += 1

  if exchange_0 == exchange_1 == pos == -1:
    return True
  else:
    return True if pos != -1 else False



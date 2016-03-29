type_1_day = 2
type_7_day = 7
type_30_day = 30

edge_1_day = 4

def solution(A):

  if len(A) < edge_1_day:
    return len(A) * type_1_day
  else:
    total = 0
    begin = 0
    while len(A) >= edge_1_day:
      end = begin + 3
      while A[end] - A[begin] < type_7_day:
        end += 1

      if end > 3:
        total += type_7_day
        A = A[end : len(A)]
        begin = end
      else:
        total += type_1_day
        A = A[begin + 1 : len(A)]
        begin += 1

    total += len(A) * type_1_day

    if total > type_30_day:
      return type_30_day
    else:
      return total



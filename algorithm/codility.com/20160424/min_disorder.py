#
## After sort one sub-sequence of array A to make the whole array is in increasing order,
##   make sure this sub-sequence is as short as it can be, write a function to get the length of this sub-sequence.
#
## The best solution should be: sort the array, then compare with the original array, then the sub-sequence is from the
##   first difference place to the last difference place.
#
def solution(A):

  disorder = []

  def order_test():
    for idx in xrange(len(A) - 1):
      if A[idx] > A[idx + 1]:
        return False
    return True

  def is_dirty(dirty_arr, e):
    for val in dirty_arr:
      if val > e:
        return True
    return False

  if order_test():
    return 0

  idx = 0
  current_dirty_seq = []
  while idx < len(A) - 1:
    if A[idx] > A[idx + 1] and len(current_dirty_seq) == 0:
      current_dirty_seq.extend([A[idx], A[idx + 1]])
      idx += 2
      continue

    if is_dirty(current_dirty_seq, A[idx]):
      current_dirty_seq.append(A[idx])
    else:
      if A[idx] > A[idx + 1]:
        disorder.append(current_dirty_seq)

        current_dirty_seq = []
        current_dirty_seq.extend([A[idx], A[idx + 1]])
        idx += 2
        continue

    idx += 1

  disorder.append(current_dirty_seq)

  counter = 0
  for e in disorder:
    counter += len(e)

  counter = counter if A[-1] >= max(A) else counter + 1

  idx_final = 0
  in_order_idx = A.index(disorder[0][0])
  while idx_final < in_order_idx:
    if A[idx_final] > A[-1]:
      counter += (in_order_idx - idx_final)
      break
    idx_final += 1

  return counter



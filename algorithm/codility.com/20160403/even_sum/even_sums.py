def solution(A):

  #
  ## 0: indicates the corresponding sequence's sum is odd number.
  ## 1: indicates the corresponding sequence's sum is even number.
  #
  statistics = {
    'seq': [],
    'status': ''
  }

  #
  ## Record all steps made by two players, until one side resign.
  #
  steps = []

  resign = 'RESIGN'

  def init_statistics():
    for d in A:
      statistics['seq'].append([d])
      if d % 2 == 0:
        statistics['status'] += '1'
      else:
        statistics['status'] += '0'

  #
  # When have two adjacent odd or even sequences, combine them.
  #
  def update_statistics():
    while True:
      idx = -1

      try:
        idx = statistics['status'].index('11')
      except ValueError, e:
        pass

      try:
        idx = statistics['status'].index('00')
      except ValueError, e:
        pass
      
      if idx != -1:
        statistics['seq'][idx] += statistics['seq'][idx + 1]
        del statistics['seq'][idx + 1]

        statistics['status'] = statistics['status'][0 : idx + 1] + statistics['status'][idx + 2 : len(statistics['status'])]
      else:
        return

  #
  ## Find longest subsequence whitch its sum is even number.
  #
  def find_longest_even_subseq(arr, sum_is_even):
    base = [arr[0 : len(arr) - 1], arr[1 : len(arr)]] if sum_is_even else [arr]

    idx = -1
    res =  []

    # From last to first
    for item in base:
      tmp = len(item)
      while tmp > 0:
        if sum(item[0 : tmp]) % 2 == 0:
          if tmp > len(res):
            res = item[0 : tmp]
            idx = 0
          break
        tmp -= 1

    # From first to last
    for item in base:
      tmp = 0
      while tmp < len(item):
        if sum(item[tmp : len(item)]) % 2 == 0:
          if len(item) - tmp > len(res):
            res = item[tmp : len(item)]
            idx = tmp
          break
        tmp += 1

    return idx, res

  def get_idx_in_A(idx_in_statistics_seq):
    real_idx = 0
    for idx, val in enumerate(statistics['seq']):
      if idx < idx_in_statistics_seq:
        real_idx += len(val)
      else:
        break
    return real_idx

  #
  ## Make one best move to win for every side.
  #
  def move():
    #
    ## Here the situation is: having even number 'even subsequences', so for win must need to find out a solution:
    ##   remove one even subsequence but keep the left even subsequences amount is still even.
    #
    if list(statistics['status']).count('1') % 2 == 0:
      longest_can_modify_idx = -1

      last_longest_even_subseq = []
      last_longest_even_subseq_idx = -1

      for idx, val in enumerate(statistics['seq']):
        if len(val) > 1 and len(val) > len(last_longest_even_subseq):
          longest_even_subseq_idx, longest_even_subseq = find_longest_even_subseq(val, True if statistics['status'][idx : idx + 1] == '1' else False)
          if len(longest_even_subseq) > len(last_longest_even_subseq):
            longest_can_modify_idx = idx
            last_longest_even_subseq = longest_even_subseq
            last_longest_even_subseq_idx = longest_even_subseq_idx

      if longest_can_modify_idx != -1:
        statistics['seq'][longest_can_modify_idx] = filter(lambda e: e not in last_longest_even_subseq, statistics['seq'][longest_can_modify_idx])

        real_idx = get_idx_in_A(longest_can_modify_idx)

        steps.append([real_idx + last_longest_even_subseq_idx, real_idx + last_longest_even_subseq_idx + len(last_longest_even_subseq) - 1])
      else:
        steps.append(resign)
        return resign

    else:
      longest_even_seq = []
      longest_even_seq_idx = -1
      for idx, val in enumerate(statistics['seq']):
        if statistics['status'][idx : idx + 1] == '1':
          if len(val) > len(longest_even_seq):
            longest_even_seq = val
            longest_even_seq_idx = idx

      if longest_even_seq_idx != -1:
        del statistics['seq'][idx]
        if longest_even_seq_idx == len(statistics['status']) - 1:
          statistics['status'] = statistics['status'][0 : longest_even_seq_idx]
        else:
          statistics['status'] = statistics['status'][0 : longest_even_seq_idx] + statistics['status'][longest_even_seq_idx + 1 : len(statistics['status'])]

        real_idx = get_idx_in_A(longest_even_seq_idx)

        steps.append([real_idx, real_idx + len(longest_even_seq) - 1])

    update_statistics()

  init_statistics()
  update_statistics()

  while True:
    try:
      statistics['status'].index('1')
      does_resign = move()
      if does_resign == resign:
        break
    except ValueError, e:
      break

  resign_idx = -1
  try:
    resign_idx = steps.index(resign)
  except ValueError, e:
    pass

  if resign_idx != -1 and resign_idx % 2 == 0:
    return 'NO SOLUTION'
  else:
    return str(steps[0][0]) + ',' + str(steps[0][1])



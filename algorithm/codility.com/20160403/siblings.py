def solution(N):
  arr = []

  for d in list(str(N)):
    arr.append(int(d))

  tmp_str = ''
  while len(arr):
    tmp_max = max(arr)
    tmp_str = tmp_str + str(tmp_max) * arr.count(tmp_max)

    arr = filter(lambda d: d != tmp_max, arr)

  return int(tmp_str) if int(tmp_str) <= 1000000000 else -1



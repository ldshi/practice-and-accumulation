# Filter out the string which its length less than 3
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
names = [name for name in names if len(name) > 3]



# Get all combinations (x, y), which x and y are both in 0 - 9, but x is an even number, y is an odd number.
[(x, y) for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 == 1]



# Get array [3, 6, 9] from M, which M is:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res_0 = [e[2] for e in M]
res_1 = [M[idx][2] for idx in (0, 1, 2)]



# Get array [1, 5, 9] from M, which M is:
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [M[idx][idx] for idx in (0, 1, 2)]



# Get the result M * N, which M and N are both matrix
M = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

N = [
  [2, 2, 2],
  [3, 3, 3],
  [4, 4, 4]
]

res = []
for idx_0, val_0 in enumerate(M):
  for idx_1, val_1 in enumerate(val_0):
    tmp_sum = 0
    idx_2 = 0
    while idx_2 < len(N):
      tmp_sum += val_1 * N[idx_2][idx_1]
      idx_2 += 1

    if len(res) > idx_0:
      res[idx_0].append(tmp_sum)
    else:
      res.append([tmp_sum])

print res



###############################################################################
bob = {'pay': 3000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
sue = {'pay': 4000, 'job': 'hdw', 'age': 45, 'name': 'Sue Jones'}
records = [bob, sue]

res = [rec['age'] + 100 if rec['age'] >= 45 else rec['age'] for rec in records]
print res



###############################################################################
###############################################################################
###############################################################################
str_arr = ['import','is','with','if','file','exception']

res = {idx: val for idx, val in enumerate(str_arr)}



###############################################################################
###############################################################################
###############################################################################
str_arr = ['a','is','with','if','file','exception']

res = {len(item) for item in str_arr}



###############################################################################
###############################################################################
###############################################################################
records = [
  ['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],  
  ['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']
]

res_0 = []
for record in records:
  for name in record:
    if name.count('e') >= 2:
      res_0.append(name)

print res_0

'''
  Different implementation.
'''
res_1 = [name for record in records for name in record if name.count('e') >= 2]

print res_1



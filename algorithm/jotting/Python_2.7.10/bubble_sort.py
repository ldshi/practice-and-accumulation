'''
  The below code just implement a very simple bubble sort, can you guess what is the result?

  Unfortunately, the result will not be like what you are expecting. It will not work!!! And
  maybe you will conclude it as: how fucking can this so weird things hapen...

  What is the reason? Can you adjust it a bit to make it work?
'''
def sort(A):
  for idx, val in enumerate(A):
    for idx_inner, val_inner in enumerate(A):
      if idx_inner > idx and val > val_inner:
        tmp = val
        A[idx] = val_inner
        A[idx_inner] = tmp
        
A = [94, 54, 67, 76, 32, 23, 8, 65, 90, 8, 6]

sort(A)

print(A)



'''
  If I adjust the above code to be like the following, then it will work, maybe you already
  know what is the reason.
'''
def sort(A):
  for idx, val in enumerate(A):
    for idx_inner, val_inner in enumerate(A):
      if idx_inner > idx and A[idx] > A[idx_inner]:
        tmp = A[idx]
        A[idx] = A[idx_inner]
        A[idx_inner] = tmp
        
A = [94, 54, 67, 76, 32, 23, 8, 65, 90, 8, 6]

sort(A)

print(A)



'''
  Do we have more elegant way to implement this?

  If I adjust the code to be like this, do you think it will work?
'''
def sort(A):
  for idx in [a for a in range(0, len(A))]:
    for idx_inner in [b for b in range(idx + 1, len(A))]:
      if A[idx] > A[idx_inner]:
        tmp = A[idx]
        A[idx] = A[idx_inner]
        A[idx_inner] = tmp

A = [94, 54, 67, 76, 32, 23, 8, 65, 90, 8, 6]

sort(A)

print(A)



'''
  If I adjust the code to be like this, do you think it will work?

  What is the difference?
'''
def sort(A):
  for idx in (a for a in range(0, len(A))):
    for idx_inner in (b for b in range(idx + 1, len(A))):
      if A[idx] > A[idx_inner]:
        tmp = A[idx]
        A[idx] = A[idx_inner]
        A[idx_inner] = tmp

A = [94, 54, 67, 76, 32, 23, 8, 65, 90, 8, 6]

sort(A)

print(A)



'''
  If you really can't understand this clearly, please go ahead and refer to this link:
    http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
'''



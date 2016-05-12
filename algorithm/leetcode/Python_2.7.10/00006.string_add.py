#
## https://leetcode.com/problems/zigzag-conversion/
#
class Solution(object):
  def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if len(s) <= numRows or numRows < 2:
      return s

    str_arr = ['' for x in range(numRows)]

    row = 0
    increase = None

    for c in s:
      str_arr[row] += c

      if row == 0 or row == numRows - 1:
        increase = not increase

      row = row + 1 if increase else row - 1

    return ''.join(x for x in str_arr)



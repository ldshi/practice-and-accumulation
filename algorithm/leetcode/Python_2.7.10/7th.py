#
## https://leetcode.com/problems/reverse-integer/
#
## 2147483647 hehe...
#
class Solution(object):
  def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if str(x).startswith('-'):
      res = int('-' + str(x)[1:][::-1])
      return 0 if res < -2147483647 else res
    else:
      res = int(str(x)[::-1])
      return 0 if res > 2147483647 else res



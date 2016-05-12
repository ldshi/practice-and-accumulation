#
## https://leetcode.com/problems/palindrome-number/
#
## -2147483648 <= x <= 2147483647
#
class Solution(object):
  def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
      return False

    if int(str(x)[::-1]) > 2147483647 or int(str(x)[::-1]) != x:
      return False

    return True



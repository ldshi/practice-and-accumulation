#
## https://leetcode.com/problems/roman-to-integer/
#

#
## Copied from: https://leetcode.com/discuss/89076/python-easy-to-understand-solution
#
class Solution(object):
  def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    res = 0

    roman_sys = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }

    chars = list(s)

    for idx in range(len(chars) - 1):
      typ = 1 if roman_sys[chars[idx]] >= roman_sys[chars[idx + 1]] else -1
      res += typ * roman_sys[chars[idx]]

    return res + roman_sys[chars[len(chars) - 1]]



#
## https://leetcode.com/problems/integer-to-roman/
#
class Solution(object):
  def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    roman_sys = {
      1: 'I',
      5: 'V',
      10: 'X',
      50: 'L',
      100: 'C',
      500: 'D',
      1000: 'M'
    }

    res, key = '', 1

    while num:
      mod = num % 10

      if mod in range(1, 4):
        res = mod * roman_sys[key] + res
      elif mod == 4:
        res = roman_sys[key] + roman_sys[5 * key] + res
      elif mod == 5:
        res = roman_sys[5 * key] + res
      elif mod in range(6, 9):
        res = roman_sys[5 * key] + (mod - 5) * roman_sys[key] + res
      elif mod == 9:
        res = roman_sys[key] + roman_sys[10 * key] + res

      key *= 10
      num /= 10

    return res



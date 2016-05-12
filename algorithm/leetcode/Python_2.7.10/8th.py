#
## https://leetcode.com/problems/string-to-integer-atoi/
#
## -2147483648 <= x <= 2147483647
#
class Solution(object):
  def myAtoi(self, str):
    """
    :type str: str
    :rtype: int
    """
    wtf = str

    if wtf is None:
      return 0

    wtf = str.strip()

    for idx, val in enumerate(wtf):
      if not val.isdigit() and val not in ['-', '+']:
        wtf = wtf[:idx]
        break

    if wtf.startswith(('-', '+')):
      if wtf[1:].isdigit():
        res = int(wtf)
        if res < -2147483648:
          return -2147483648
        elif res > 2147483647:
          return 2147483647
        else:
          return res
      else:
        return 0
    else:
      if wtf.isdigit():
        res = int(wtf)
        return 2147483647 if res > 2147483647 else res
      else:
        return 0



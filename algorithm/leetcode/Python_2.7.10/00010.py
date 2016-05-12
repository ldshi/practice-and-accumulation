#
## https://leetcode.com/problems/regular-expression-matching/
#

#
## The question itself is not well defined, and the assesment procedure also performed weirdly,
##   take the following test case:
##     'a.*cc'
##     'abbcc'
##   the assesment procedure expects 'False', but according to the scanty definitions, the result should be 'True'
##   explanations:
##     1. '.' represents for 'b', then '*' will also represent for 'b', then the first str will be: 'abbcc'.
##     2. It exactly matches the second str 'abbcc'.
#
## So, no point to waste time on thinking about this question.
#
class Solution(object):
  def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    def rm_leading_stars(s):
      for idx, val in enumerate(s):
        if val != '*':
          return s[idx:]

    def omit_continuous_stars(s):
      res = s[0]
      for idx in range(1, len(s)):
        if s[idx] == '*':
          if res[-1] != '*':
            res += s[idx]
        else:
          res += s[idx]
      return res

    def move(target, cur_pos, match):


    if s is None or p is None:
      raise ValueError('All parameters should be str.')

    s = rm_leading_stars(s)
    p = rm_leading_stars(p)

    s = omit_continuous_stars(s)
    p = omit_continuous_stars(s)



#
## https://leetcode.com/problems/longest-palindromic-substring/
#
class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if s is None:
      raise ValueError('Input must be a String.')

    if len(s) == 0 or len(s) == 1:
      return s

    if len(s) == 2:
      return s if s[0] == s[1] else s[1]

    #
    ##        0 1 2 3 4 5
    ##        a b c c b a
    ##
    ##  0 a   * * * * * *
    ##  1 b   O * * * * *
    ##  2 c   J N * * * *
    ##  3 c   F I M * * *
    ##  4 b   C E H L * *
    ##  5 a   A B D G K *
    ##
    ## Watch the iteration order: A B C D E F G...
    ##   just try to return as early as possible.
    #
    for c in range(len(s) - 1):
      x = len(s) - 1
      y = c
      while y >= 0:
        if s[y : x + 1] == s[y : x + 1][::-1]:
          return s[y : x + 1]
        x -= 1
        y -= 1

    return s[-1]



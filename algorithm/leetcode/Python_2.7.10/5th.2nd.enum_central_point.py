#
## https://leetcode.com/problems/longest-palindromic-substring/
#
class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    def search_palindrome(start, end, target = s):
      while start >= 0 and end < len(target) and target[start] == target[end]:
        start -= 1
        end += 1
      return target[start + 1 : end]


    if s is None:
      raise ValueError('Input must be a String.')

    if len(s) == 0 or len(s) == 1:
      return s

    if len(s) == 2:
      return s if s[0] == s[1] else s[1]

    res = s[-1]

    for idx in range(len(s)):
      tmp = search_palindrome(idx, idx)

      if len(tmp) > len(res):
        res = tmp

      tmp = search_palindrome(idx, idx + 1)

      if len(tmp) > len(res):
        res = tmp

    return res



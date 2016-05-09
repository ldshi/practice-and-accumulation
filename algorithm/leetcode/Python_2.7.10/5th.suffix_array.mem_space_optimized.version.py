#
## https://leetcode.com/problems/longest-palindromic-substring/
#

#
## On test case 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
##   still run into Memory Limit Exceeded  problem, through already optimized the memory space using a lot.
#
class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    def get_common_prefix(s_0, s_1):
      if s_0.startswith(s_1):
        return (len(s_1), s_1)

      if s_1.startswith(s_0):
        return (len(s_0), s_0)

      for idx in range(min(len(s_0), len(s_1))):
        if s_0[idx] != s_1[idx]:
          return (idx, s_0[0 : idx])

      return (0, '')

    if s is None:
      raise ValueError('Input must be a String.')

    if len(s) < 2:
      return s

    if len(s) < 3:
      return s if s[0] is s[1] else s[1]

    modified_s = s + '#' + s[::-1]

    len_of_modified_s = len(modified_s)

    suffix_arr = range(len_of_modified_s)

    suffix_arr.sort(key = lambda x : modified_s[x : len_of_modified_s])

    found_longest_common_prefix = s[-1]
    found_longest_common_prefix_len = 1

    idx = len(suffix_arr) - 1
    while idx > 0:
      if len(modified_s[suffix_arr[idx] : len_of_modified_s]) >= found_longest_common_prefix_len and len(modified_s[suffix_arr[idx - 1] : len_of_modified_s]) >= found_longest_common_prefix_len:
        common_prefix_len, common_prefix = get_common_prefix(modified_s[suffix_arr[idx] : len_of_modified_s], modified_s[suffix_arr[idx - 1] : len_of_modified_s])
        if common_prefix_len > found_longest_common_prefix_len:
          #
          ## Why add this check?
          ## Refer to this example:
          ##   s = 'abacdfgdcaba', then reverted_s = 'abacdgfdcaba', then the LCS will be: 'abacd', apparently, this is wrong answer.
          #
          if common_prefix == common_prefix[::-1]:
            found_longest_common_prefix = common_prefix
            found_longest_common_prefix_len = common_prefix_len

      idx -= 1

    return found_longest_common_prefix



s = Solution()
s.longestPalindrome('aabcaa')



#
## https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
class Solution(object):
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    if s is None:
      raise ValueError('Parameter should be a String.')

    if len(s) < 2:
      return len(s)

    start = last_max_len = 0

    for idx in range(len(s) - 1):
      if s[idx + 1] in s[start : idx + 1]:
        if idx - start + 1 > last_max_len:
          last_max_len = idx - start + 1

        start = start + s[start : idx + 1].index(s[idx + 1]) + 1

    final_seq_len = len(s) - start

    return final_seq_len if final_seq_len > last_max_len else last_max_len

s = Solution();
s.lengthOfLongestSubstring('dvdf')



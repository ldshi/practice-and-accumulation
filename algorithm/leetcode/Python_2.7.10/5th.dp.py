#
## https://leetcode.com/problems/longest-palindromic-substring/
#

#
## On test case 'lcnvoknqgejxbfhijmxglisfzjwbtvhodwummdqeggzfczmetrdnoetmcydwddmtubcqmdjwnpzdqcdhplxtezctvgnpobnnscrmeqkwgiedhzsvskrxwfyklynkplbgefjbyhlgmkkfpwngdkvwmbdskvagkcfsidrdgwgmnqjtdbtltzwxaokrvbxqqqhljszmefsyewwggylpugmdmemvcnlugipqdjnriythsanfdxpvbatsnatmlusspqizgknabhnqayeuzflkuysqyhfxojhfponsndytvjpbzlbfzjhmwoxcbwvhnvnzwmkhjxvuszgtqhctbqsxnasnhrusodeqmzrlcsrafghbqjpyklaaqximcjmpsxpzbyxqvpexytrhwhmrkuybtvqhwxdqhsnbecpfiudaqpzsvfaywvkhargputojdxonvlprzwvrjlmvqmrlftzbytqdusgeupuofhgonqoyffhmartpcbgybshllnjaapaixdbbljvjomdrrgfeqhwffcknmcqbhvulwiwmsxntropqzefwboozphjectnudtvzzlcmeruszqxvjgikcpfclnrayokxsqxpicfkvaerljmxchwcmxhtbwitsexfqowsflgzzeynuzhtzdaixhjtnielbablmckqzcccalpuyahwowqpcskjencokprybrpmpdnswslpunohafvminfolekdleusuaeiatdqsoatputmymqvxjqpikumgmxaxidlrlfmrhpkzmnxjtvdnopcgsiedvtfkltvplfcfflmwyqffktsmpezbxlnjegdlrcubwqvhxdammpkwkycrqtegepyxtohspeasrdtinjhbesilsvffnzznltsspjwuogdyzvanalohmzrywdwqqcukjceothydlgtocukc'
##   still run into exceeding time limitation problem, through the performance alread got improved a lot: about 200ms
#
class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if s is None:
      raise ValueError('Input must be a String.')

    if len(s) < 2:
      return s

    if len(s) < 3:
      return s if s[0] is s[1] else s[1]

    matrix = [[0 for col in range(len(s))] for row in range(len(s))]

    reverted_s = s[::-1]

    idx_x, idx_y = -1, -1
    found_longest_palindrome_str_len = 0

    for idx, val in enumerate(s):
      for idx_inner, val_inner in enumerate(reverted_s):
        if val == val_inner:
          if idx > 0 and idx_inner > 0:
            matrix[idx][idx_inner] = matrix[idx - 1][idx_inner - 1] + 1
          else:
            matrix[idx][idx_inner] = 1

          if matrix[idx][idx_inner] > found_longest_palindrome_str_len:
            #
            ## Why add this check?
            ## Refer to this example:
            ##   s = 'abacdfgdcaba', then reverted_s = 'abacdgfdcaba', then the LCS will be: 'abacd', apparently, this is wrong answer.
            #
            tmp = s[idx - matrix[idx][idx_inner] + 1 : idx + 1]
            if tmp == tmp[::-1]:
              found_longest_palindrome_str_len = matrix[idx][idx_inner]
              idx_x, idx_y = idx, idx_inner

    if found_longest_palindrome_str_len == 0:
      return s[-1]
    else:
      return s[idx_x - found_longest_palindrome_str_len + 1 : idx_x + 1]

s = Solution()
s.longestPalindrome('lcnvoknqgejxbfhijmxglisfzjwbtvhodwummdqeggzfczmetrdnoetmcydwddmtubcqmdjwnpzdqcdhplxtezctvgnpobnnscrmeqkwgiedhzsvskrxwfyklynkplbgefjbyhlgmkkfpwngdkvwmbdskvagkcfsidrdgwgmnqjtdbtltzwxaokrvbxqqqhljszmefsyewwggylpugmdmemvcnlugipqdjnriythsanfdxpvbatsnatmlusspqizgknabhnqayeuzflkuysqyhfxojhfponsndytvjpbzlbfzjhmwoxcbwvhnvnzwmkhjxvuszgtqhctbqsxnasnhrusodeqmzrlcsrafghbqjpyklaaqximcjmpsxpzbyxqvpexytrhwhmrkuybtvqhwxdqhsnbecpfiudaqpzsvfaywvkhargputojdxonvlprzwvrjlmvqmrlftzbytqdusgeupuofhgonqoyffhmartpcbgybshllnjaapaixdbbljvjomdrrgfeqhwffcknmcqbhvulwiwmsxntropqzefwboozphjectnudtvzzlcmeruszqxvjgikcpfclnrayokxsqxpicfkvaerljmxchwcmxhtbwitsexfqowsflgzzeynuzhtzdaixhjtnielbablmckqzcccalpuyahwowqpcskjencokprybrpmpdnswslpunohafvminfolekdleusuaeiatdqsoatputmymqvxjqpikumgmxaxidlrlfmrhpkzmnxjtvdnopcgsiedvtfkltvplfcfflmwyqffktsmpezbxlnjegdlrcubwqvhxdammpkwkycrqtegepyxtohspeasrdtinjhbesilsvffnzznltsspjwuogdyzvanalohmzrywdwqqcukjceothydlgtocukc')



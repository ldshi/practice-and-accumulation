#
## https://leetcode.com/problems/longest-palindromic-substring/
#

#
## On test case 'zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir'
##   the algorithm running time is about 650ms, exceeds the time limitation, cannot find a way to significantly improve the performance.
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

    accumulation = {0: ''}

    for idx in range(1, len(s) - 1):
      l_len = idx
      r_len = len(s) - idx - 1

      is_left_ctrl = True if l_len <= r_len else False

      x_range = min(l_len, r_len)

      tmp_start = int((max(accumulation) - 1) / 2)
      start = tmp_start if tmp_start > 1 else 1

      for r in range(start, x_range + 1):

        # This condition can be improved, but will not significantly improve the performance.
        if x_range + 1 + x_range + 1 <= max(accumulation):
          break

        if r + 1 + r <= max(accumulation) or r + 1 + r + 1 <= max(accumulation):
          continue

        sub_str = s[idx - r : idx + r + 1]

        if sub_str == sub_str[::-1]:
          accumulation[r + 1 + r] = sub_str

        if is_left_ctrl:
          sub_str = s[idx - r : idx + r + 2]
          if sub_str == sub_str[::-1]:
            accumulation[r + 1 + r + 1] = sub_str
        else:
          sub_str = s[idx - r - 1 : idx + r + 1]
          if sub_str == sub_str[::-1]:
            accumulation[r + 1 + 1 + r] = sub_str

    tmp_key = max(accumulation)

    return s[-1] if tmp_key == 0 else accumulation[tmp_key]

s = Solution()
s.longestPalindrome('zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir')



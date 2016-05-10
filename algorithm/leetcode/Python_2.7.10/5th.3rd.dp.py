#
## https://leetcode.com/problems/longest-palindromic-substring/
#

#
## Unfortunately, still run into 'Runtime exceeds limitation' error, don't know how to improve.
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

    matrix = [[1 if col == row else None for col in range(len(s))] for row in range(len(s))]

    res_x = res_y = -1

    c = len(s) - 1
    while c > 0:
      x = 0
      y = len(s) - c
      while x < c and y <= c:
        if c == len(s) - 1:
          if s[x] == s[y]:
            matrix[x][y] = 1
            res_x = x
            res_y = y
          else:
            matrix[x][y] = 0
        else:
          if s[x] == s[y] and matrix[x + 1][y - 1]:
            matrix[x][y] = 1
            res_x = x
            res_y = y
          else:
            matrix[x][y] = 0
        x += 1
        y += 1
      c -= 1

    return s[-1] if res_x == -1 else s[res_x : res_y + 1]

s = Solution()
s.longestPalindrome('anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg')



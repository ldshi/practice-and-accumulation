#
## https://leetcode.com/problems/container-with-most-water/
#
class Solution(object):
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    if height is None or len(height) < 2:
      raise ValueError('Invalid input.')

    max_cap = 0
    idx_l = 0
    idx_r = len(height) - 1

    while idx_r > idx_l:
      if height[idx_l] < height[idx_r]:
        tmp = height[idx_l] * (idx_r - idx_l)
        if tmp > max_cap:
          max_cap = tmp

        idx_l += 1
      elif height[idx_l] == height[idx_r]:
        tmp = height[idx_l] * (idx_r - idx_l)
        if tmp > max_cap:
          max_cap = tmp

        idx_l += 1
        idx_r -= 1
      else:
        tmp = height[idx_r] * (idx_r - idx_l)
        if tmp > max_cap:
          max_cap = tmp
          
        idx_r -= 1

    return max_cap



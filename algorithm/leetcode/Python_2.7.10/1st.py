#
## https://leetcode.com/problems/two-sum/
#
class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for idx, val in enumerate(nums):
      if target - val in nums[idx + 1 : len(nums)]:
        return [idx, nums[idx + 1 : len(nums)].index(target - val) + idx + 1]


        
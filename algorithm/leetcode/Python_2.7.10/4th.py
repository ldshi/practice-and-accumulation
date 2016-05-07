#
## https://leetcode.com/problems/median-of-two-sorted-arrays/
#
class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    if nums1 is None or nums2 is None:
      raise ValueError('Inputs should be arrays.')

    total_len = len(nums1) + len(nums2)

    if total_len == 0:
      raise ValueError('Two arrays cannot both be empty.')

    is_even = True if total_len % 2 == 0 else False

    median = [None, None]

    if is_even:
      median[1] = int(total_len / 2)
      median[0] = median[1] - 1
    else:
      median[0] = int((total_len - 1) / 2)

    if len(nums1) == 0:
      if is_even:
        return (nums2[median[0]] + nums2[median[1]]) / 2.0
      else:
        return nums2[median[0]]

    if len(nums2) == 0:
      if is_even:
        return (nums1[median[0]] + nums1[median[1]]) / 2.0
      else:
        return nums1[median[0]]

    median_sum = idx_1 = idx_2 = 0

    while True:
      if median[0] is None and median[1] is None:
        break

      if idx_1 == len(nums1):
        if median[0] is not None and idx_1 + idx_2 == median[0]:
          median_sum += nums2[idx_2]

          if median[1] is not None:
            median_sum += nums2[idx_2 + 1]

          break

        if median[1] is not None and idx_1 + idx_2 == median[1]:
          median_sum += nums2[idx_2]
          break

        idx_2 += 1

        continue

      if idx_2 == len(nums2):
        if median[0] is not None and idx_1 + idx_2 == median[0]:
          median_sum += nums1[idx_1]

          if median[1] is not None:
            median_sum += nums1[idx_1 + 1]

          break

        if median[1] is not None and idx_1 + idx_2 == median[1]:
          median_sum += nums1[idx_1]
          break

        idx_1 += 1

        continue

      if nums1[idx_1] == nums2[idx_2]:
        if median[0] is not None and idx_1 + idx_2 == median[0] - 1:
          median_sum += nums1[idx_1]

          median[0] = None

        if idx_1 + idx_2 == median[0]:
          median_sum += nums1[idx_1]

          median[0] = None

          if median[1] is not None:
            median_sum += nums2[idx_2]
            break

        if idx_1 + idx_2 == median[1] and median[1] is not None:
          median_sum += nums1[idx_1]
          break

        idx_1 += 1
        idx_2 += 1

      elif nums1[idx_1] > nums2[idx_2]:
        if median[0] is not None and idx_1 + idx_2 == median[0]:
          median_sum += nums2[idx_2]

          idx_2 += 1

          median[0] = None

          continue

        if median[1] is not None and idx_1 + idx_2 == median[1]:
          median_sum += nums2[idx_2]
          break

        idx_2 += 1

      else:
        if median[0] is not None and idx_1 + idx_2 == median[0]:
          median_sum += nums1[idx_1]

          idx_1 += 1

          median[0] = None

          continue

        if median[1] is not None and idx_1 + idx_2 == median[1]:
          median_sum += nums1[idx_1]
          break

        idx_1 += 1

    return median_sum / 2.0 if is_even else median_sum

s = Solution()
s.findMedianSortedArrays([1, 2], [1, 2])



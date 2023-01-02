from typing import List


class Solution:
  def max_sub_array_util(
    self, 
    nums: List[int], 
    left: int, 
    right: int
  ) -> int:

    if left > right: 
      return -inf

    mid, left_sum, right_sum, cur_sum = (left + right) // 2, 0, 0, 0

    for i in range(mid-1, left-1, -1):
      left_sum = max(left_sum, cur_sum := cur_sum + nums[i])

    cur_sum = 0
    for i in range(mid+1, right+1):
      right_sum = max(right_sum, cur_sum := cur_sum + nums[i])

    return max(
      self.max_sub_array_util(nums, left, mid-1), 
      self.max_sub_array_util(nums, mid+1, right), 
      left_sum + nums[mid] + right_sum
    )

  def maxSubArray(self, nums: List[int]) -> int:
    return self.max_sub_array_util(nums, 0, len(nums) - 1)
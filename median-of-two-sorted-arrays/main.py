from typing import List


def merge(
  nums1: List[int], 
  nums2: List[int], 
  n1: int, 
  n2: int
) -> List[int]:
    nums3 = [None] * (n1 + n2)
    i = j = k = 0

    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            nums3[k] = nums1[i]
            k = k + 1
            i = i + 1
        else:
            nums3[k] = nums2[j]
            k = k + 1
            j = j + 1

    while i < n1:
        nums3[k] = nums1[i]
        k = k + 1
        i = i + 1

    while j < n2:
        nums3[k] = nums2[j]
        k = k + 1
        j = j + 1

    return nums3


def median(nums: List[int]) -> int:
    half, odd = divmod(len(nums), 2)
    if odd:
        return nums[half]
    return (nums[half - 1] + nums[half]) / 2


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums3 = self.merge(nums1, nums2, len(nums1), len(nums2))
    return self.median(nums3)


if __name__ == "__main__":
    nums1 = []
    nums2 = []
    
    print(findMedianSortedArrays(nums1, nums2))

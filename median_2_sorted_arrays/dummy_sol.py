import statistics
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    combined_nums = []

    if nums1:
        combined_nums += nums1

    if nums2: 
        combined_nums += nums2

    combined_nums.sort()

    return statistics.median(combined_nums)
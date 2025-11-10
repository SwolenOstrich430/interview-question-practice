from typing import List

'''
    Planning; 
        - get length of both lists 
            - if odd, just need the total_len / 2 for index 
            - if even, need average of the split numbers?
        - loop through range of 0 to median index 
            - create two vars to track current index in both lists 
                - curr_nums1_ind
                - curr_nums2_ind
            - if nums1[curr_nums1_ind] >= nums2[curr_nums2_ind]
                - curr_nums1_ind += 1
            - if nums1[curr_nums1_ind] =< nums2[curr_nums2_ind]
                - curr_nums2_ind += 1
        - check if curr_nums1_ind + curr_nums2_ind == median
            - return the 
'''
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    median_index = float((len(nums1) + len(nums2))) / 2.0

    nums1_ind = 0
    nums2_ind = 0
    last_num = None
    penult_num = None

    for i in range((int(median_index) + 1)):
        if last_num != None: 
            penult_num = last_num

        if nums1_ind < len(nums1) and nums2_ind < len(nums2):
            if nums1[nums1_ind] <= nums2[nums2_ind]:
                last_num = nums1[nums1_ind]
                nums1_ind += 1
            else:
                last_num = nums2[nums2_ind]
                nums2_ind += 1
        elif nums1_ind < len(nums1):
            last_num = nums1[nums1_ind]
            nums1_ind += 1
        elif nums2_ind < len(nums2):
            last_num = nums2[nums2_ind]
            nums2_ind += 1
    
        
    if int(median_index) == median_index:
        last_num = float(last_num + penult_num) / 2.0

    return last_num

findMedianSortedArrays(
    [1,3],
    [2]
)
'''
Example Input: 
    - "babad"
Planning: 
    - keep an array to hold start and stop indexes for current substr
    subtr_indexes = []

    - starting at index 1:
        - check +- index bounds are inline
            - if no, increment i
        - if i - 1 == i + 1 
            - increment num to add/substract 
        - else 
            - check curr substring range vs. subtr_indexes
                - if greater range, increment 
            - increment i
'''
def longestPalindrome(s: str) -> str:
    substr_indexes = [0, 0]
    curr_substr_indexes = [0, 0]
    pl_min_index = 1
    arr_len = len(s[1:])

    for i in range(1, len(s[1:])):
        while (i - pl_min_index >= 0 and i + pl_min_index <= arr_len - 1):
            if s[i - pl_min_index] == s[i + pl_min_index]:
                curr_substr_indexes[0] = i - pl_min_index
                curr_substr_indexes[1] = i + pl_min_index
            elif s[i] == s[i + pl_min_index] and curr_substr_indexes[0] == 0 and curr_substr_indexes[1] == 0:
                curr_substr_indexes[0] = i 
                curr_substr_indexes[1] = i + pl_min_index
            elif s[i - pl_min_index] == s[i] and curr_substr_indexes[0] == 0 and curr_substr_indexes[1] == 0:
                curr_substr_indexes[0] = i - pl_min_index
                curr_substr_indexes[1] = i
            else: 
                break

            pl_min_index += 1

        if (len(substr_indexes) == 0 or 
            (curr_substr_indexes[1] - curr_substr_indexes[0]) > (substr_indexes[1] - substr_indexes[0])):
            substr_indexes = curr_substr_indexes

        curr_substr_indexes = [0, 0]
        pl_min_index = 1

    return s[substr_indexes[0]:substr_indexes[1] + 1]

longestPalindrome("cbbd")
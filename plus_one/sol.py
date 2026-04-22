class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return 

        carry = 1
        idx = len(digits) - 1

        while carry is None or carry > 0:
            if idx < 0:
                digits.insert(0, carry)
                break 

            last_sum = digits[idx] + carry
            carry = last_sum // 10

            if carry == 0:
                digits[idx] = last_sum 
            else:
                digits[idx] = last_sum % 10

            idx -= 1

        return digits

        


        
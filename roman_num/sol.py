class Solution(object):
    def intToRoman(self, num):
        """
            * starting from the ones place and moving forward in tens place
            * if val is: 
                - 0: skip
                - 4: get 1-value|5-value
                - 5: get 5-value
                - 9: get 1-value|10-value
                - else: get num*1-value
        """
        dup_num = int(num)
        converted_num = "" 
        curr_power = 0
        curr_num = 0
        curr_char = None

        while dup_num > 0:
            curr_num = int(dup_num) % int(10)

            if curr_num == 0:
                pass
            elif curr_num < 4:
                curr_char = self.get_roman_numeral(1, curr_power)
                converted_num = (curr_char * curr_num) + converted_num
            elif curr_num == 4:
                curr_char = self.get_roman_numeral(5, curr_power)
                converted_num = curr_char + converted_num
                
                curr_char = self.get_roman_numeral(1, curr_power)
                converted_num = curr_char + converted_num
            elif curr_num == 5:
                curr_char = self.get_roman_numeral(5, curr_power)
                converted_num = curr_char + converted_num
            elif curr_num == 9:
                curr_char = self.get_roman_numeral(10, curr_power)
                converted_num = curr_char + converted_num
                
                curr_char = self.get_roman_numeral(1, curr_power)
                converted_num = curr_char + converted_num
            elif curr_num > 5 and curr_num < 9:
                curr_char = self.get_roman_numeral(5, curr_power)
                converted_num = curr_char + converted_num

                curr_char = self.get_roman_numeral(1, curr_power)
                converted_num = (curr_char * (int(curr_num) - int(5))) + converted_num
                
            dup_num = int(dup_num) / int(10)
            curr_power += 1

        return converted_num

    def get_roman_numeral(self, num, power):
        if power == 0:
            converted_num = num
        else:
            converted_num = num * (10**power)

        assert converted_num in self.roman_numeral_map()

        return self.roman_numeral_map()[converted_num]
        
    def roman_numeral_map(self):
        return {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        

sol = Solution()
sol.intToRoman(10)
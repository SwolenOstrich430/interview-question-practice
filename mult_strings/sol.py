class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # return str(int(num1) * int(num2))
        
        if num1 == "0" or num2 == "0":
            return "0" 
        
        num1_as_num = 0  
        num2_as_num = 0 

        for i in range(len(num1)):
            if num1_as_num == 0 and num1[i] == "0":
                continue 

            num1_as_num *= 10 
            num1_as_num += int(num1[i])

        for i in range(len(num2)):
            if num1_as_num == 0 and num1[i] == "0":
                continue 

            num2_as_num *= 10 
            num2_as_num += int(num2[i])

        final_num = num1_as_num * num2_as_num 
        final_num_as_str = ""

        while final_num > 0:
            # 491555843274052692
            print(final_num)
            final_num_as_str = f"{final_num % 10}{final_num_as_str}"
            final_num = int(final_num // 10)

        return final_num_as_str


sol = Solution() 

test_cases = [
    ["6913259244", "71103343", "491555843274052692"],
    ["2", "3", "6"]
]

for test_case in test_cases:
    if sol.multiply(test_case[0], test_case[1]) != test_case[2]:
        raise 
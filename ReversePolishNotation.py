class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in tokens:
            if i.strip("-").isdigit():
                nums.append(int(i))
            else:
                a = nums.pop()
                b = nums.pop()
                if i == "/":
                    temp = b/a
                    if temp > 0:
                        temp = math.floor(temp)
                    else:
                        temp = math.ceil(temp)
                else:
                    temp  = eval(str(b) + i + str(a))
                nums.append(temp)
                
        return nums[0]

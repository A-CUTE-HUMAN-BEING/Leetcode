class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

Solution = Solution()
print(Solution.addBinary("11","1"))
#100
# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
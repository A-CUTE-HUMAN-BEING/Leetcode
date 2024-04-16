class Solution :
    def reverse(self, x: int) -> int :
        if x == 0 :
            return 0
        elif str(x)[0] == '-' :
            if int('-' + str(x)[:0 : -1]) < -2 **31 :
                return 0
            return int('-' + str(x)[:0 : -1])
        else:
            if int(str(x)[:: - 1]) > 2 **31 - 1 :
                return 0
            return int(str(x)[:: - 1])

Solution = Solution()
print(Solution.reverse(123))
print(Solution.reverse(-123))
print(Solution.reverse(120))
print(Solution.reverse(0))
print(Solution.reverse(1534236469))

# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#
# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
#
# 假设环境不允许存储 64 位整数（有符号或无符号）。
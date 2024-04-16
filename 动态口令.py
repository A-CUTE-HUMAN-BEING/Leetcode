class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        a=password[:target]
        return password[target:]+a

Solution = Solution()
print(Solution.dynamicPassword("abcdefg",2))
print(Solution.dynamicPassword("lrloseumgh",6))
print(Solution.dynamicPassword("leetcode",8))

# cdefgab
# umghlrlose
# leetcode


# 某公司门禁密码使用动态口令技术。初始密码为字符串 password，密码更新均遵循以下步骤：
# 设定一个正整数目标值 target
# 将 password 前 target 个字符按原顺序移动至字符串末尾
# 请返回更新后的密码字符串。
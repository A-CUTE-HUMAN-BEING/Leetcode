class Solution:
    def isUnique(self, astr: str) -> bool:
        for i in astr:
            if(astr.count(i)!=1):
                return False
        return True
Solution = Solution()
print(Solution.isUnique("leetcode"))
print(Solution.isUnique("abc"))
print(Solution.isUnique("a"))
# False
# True
# True

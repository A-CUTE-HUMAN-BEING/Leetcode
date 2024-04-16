from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if(nums[0]==1):
            return 0
        for i in range(0,len(nums)-1):
            if nums[i+1]!=nums[i]+1:
                return nums[i]+1
        return nums[-1]+1

Solution = Solution()
print(Solution.missingNumber([3,0,1]))
print(Solution.missingNumber([0,1]))

#数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？



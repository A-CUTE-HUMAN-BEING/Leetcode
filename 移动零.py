from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 初始化一个指针 i，用于追踪非零元素的位置
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num  # 将非零元素移到前面
                i += 1

        # 将剩余的位置填充零
        while i < len(nums):
            nums[i] = 0
            i += 1
        return nums
Solution = Solution()
print(Solution.moveZeroes([0,1,0,3,12]))
# [1, 3, 12, 0, 0]

# 给定一个数组nums，编写一个函数将所有0
# 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。


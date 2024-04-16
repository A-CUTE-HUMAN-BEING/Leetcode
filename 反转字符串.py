from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]

Solution = Solution()
s = ["h","e","l","l","o"]
Solution.reverseString(s)
# print(s)#['o', 'l', 'l', 'e', 'h']

# #s[:]=s[::-1]和s=s[::-1]区别

s ="hello"
s = s[::-1]
print(s)
# print(t)


s = ["h","e","l","l","o"]
t= s[::-1]
print(t)
print(s)



#s[:]=s[::-1]是将s的元素逆序，s的地址不变
#s=s[::-1]是将s的地址指向逆序后的地址，s的地址改变
#s[:]=s[::-1]是在原地址上进行操作，s=s[::-1]是新开辟一个地址进行操作

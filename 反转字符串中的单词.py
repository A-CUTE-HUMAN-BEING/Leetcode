class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1=[]
        for i in s.split():
            list1.append(i[::-1])
        return ' '.join(list1)
print(Solution().reverseWords("Let's take LeetCode contest"))
# s'teL ekat edoCteeL tsetnoc

# 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
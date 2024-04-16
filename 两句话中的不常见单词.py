from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = s1.split()
        l2 = s2.split()
        list1 = []
        for i in l1:
            if (i not in l2) and (l1.count(i) == 1):
                list1.append(i)
        for i in l2:
            if (i not in l1) and (l2.count(i) == 1):
                list1.append(i)
        return list1
Solution = Solution()
print(Solution.uncommonFromSentences("this apple is sweet","this apple is sour"))
print(Solution.uncommonFromSentences("apple apple","banana"))

# ['sweet', 'sour']
# ['banana']

# 句子 是一串由空格分隔的单词。每个 单词 仅由小写字母组成。
#
# 如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。
#
# 给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。
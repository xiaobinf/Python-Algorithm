'''
leetcode 720
'''
class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        ans=''
        words=set(words)
        for word in words:
            if len(word)>len(ans) or (len(word)==len(ans) and word<ans):
                if all([word[:i] in words for i in range(1,len(word))]):
                    ans=word
        return ans

s=Solution()
words=["w","wo","wor","worl", "world"]
words_1=["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(s.longestWord(words_1))
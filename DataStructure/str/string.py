class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h = len(haystack)
        n = len(needle)
        for i in range(h - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1

    def divide(self, dividend, divisor):
        """
        :type dividend: int 被除数
        :type divisor: int 除数
        :rtype: int
        """

    def reverseString(self,s):
        l=len(s)
        if l<2:
            return s
        return self.reverseString(s[l//2:])+self.reverseString(s[:l//2])

    # 含有额外的空间
    def reverseString_2(self,s):
        l=len(s)
        s1=list(s)
        i,j=0,l-1
        while i<j:
            s1[i],s1[j]=s1[j],s1[i]
            i+=1
            j-=1
        return ''.join(s1)

    def onlyNumOrChar(self,s):
        l=list()
        s=s.lower()
        for i in s:
            if i in 'abcdefghijklmnopqrstuvwxyz0123456789':
                l.append(i)
        return ''.join(l)
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=self.onlyNumOrChar(s)
        if s==s[::-1]:
            return True
        return False

    def isPalindrome_2(self,s):
        i,j=0,len(s)-1
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i].lower()!= s[j].lower():
                return False
            i+=1
            j-=1
        return True

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d={'U':0,'D':0,'L':0,'R':0}
        for i in moves:
            if d.get(i) is 0:
                d[i]=1
            else:
                d[i]+=1
        if d['U']==d['D'] and d['L']==d['R']:
            return True
        return False


    def generateP(self,n):
        if n is 1:
            return '()'
        if n is 2:
            return '()()'
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n is 1:
            return

    def longestCommonPrefix(self, strs):
        """
        leetcode 14 Longest Common Prefix
        :type strs: List[str]
        :rtype: str
        """
        strs=list(set(strs))
        if strs==[] or '' in strs:
            return ''
        if len(strs)==1:
            return strs[0]
        str=''
        minlen=len(strs[0])
        for stri in strs:
            if minlen>len(stri):
                minlen=len(stri)
        for i in range(1,minlen+1):
            s=set([stri[:i] for stri in strs])
            if len(s)==1:
                str=list(s)[0]
        return str

    def lengthOfLongestSubstring(self, s):
        """
        leetcode 3 Longest Substring Without Repeating Characters
        需要改进  是否可以加入随机算法
        :type s: str
        :rtype: int
        """
        if s=='': return 0
        if len(s)==1: return 1
        l=list()
        for i in range(len(s)):
            lens=1
            for j in range(i+1,len(s)):
                # 还有优化的空间
                if s[j] in s[i:j]:
                    break
                else:
                    lens+=1
            l.append(lens)
            # print(l)
        return max(l)

    def removeElement(self, nums, val):
        """
        leetcode 27 Remove Element
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i

    def searchInsert(self, nums, target):
        """
        35 Search Insert Position
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        for j in range(len(nums)):
            if nums[j]<target:
                i+=1
            elif nums[j]==target:
                return i
            else:
                return i
        return i

    def lengthOfLastWord(self, s):
        """
        58
        :type s: str
        :rtype: int
        """
        if s.split() == []:
            return 0
        strs=s.split()
        return len(strs[-1:][0])







s=Solution()
print(s.lengthOfLastWord(" "))
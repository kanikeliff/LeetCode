class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        first= strs[0]
        last=strs[-1]
        i=0
        min1= min(len(first),len(last))
        while i < min1 and first[i]==last[i]:
            i += 1
        return first[:i]
        


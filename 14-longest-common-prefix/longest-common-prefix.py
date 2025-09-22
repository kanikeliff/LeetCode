class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            current_char = strs[0][i]
            if any(s[i] != current_char for s in strs[1:]):
                return strs[0][:i]
    
        return strs[0][:min_len]
        


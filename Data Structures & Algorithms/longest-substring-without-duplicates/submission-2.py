class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        end=0
        max_string=0
        d={}
        while end < len(s):
            if s[end] in d and d[s[end]]>=start:
                start=d[s[end]]+1
            max_string=max(max_string,end-start+1)
            d[s[end]]=end
            end+=1
        return max_string
        
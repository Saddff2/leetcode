class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() 
        left = 0 
        big = 0  
        
        for right in range(len(s)):  
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            big = max(big, right - left + 1)
        
        return big

param_1 = "abcabcbb"
ret = Solution().lengthOfLongestSubstring(param_1)
print(ret) 
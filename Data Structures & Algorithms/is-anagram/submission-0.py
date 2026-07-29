from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort = sorted(s)
        t_sort = sorted(t)
        if s_sort == t_sort: 
            return True 
        else:
            return False

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
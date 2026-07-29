from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) < len(nums):
            return True 
        else: 
            return False

nums = [1, 2, 3, 4, 5, 6]
solution = Solution()          # create an instance
print(solution.hasDuplicate(nums))

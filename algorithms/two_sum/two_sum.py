from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) < 2 or len(nums) > 10**4) and (target < -10**9 or target > 10**9):
            return None
        for num in nums:
            if num < -10**9 or num > 10**9:
                return None
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return None
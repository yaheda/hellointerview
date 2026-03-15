from typing import List


class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] == 0:
                nums.append(0)
                nums.pop(left)
                right -= 1
            else:
                left += 1
        
        return
    
    def moveZeroes(self, nums: List[int]) -> None:
        nextNonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0: # swap
                nums[nextNonZero], nums[i] = nums[i], nums[nextNonZero]
                nextNonZero += 1
        return

solution = Solution()
nums = [2,0,4,0,9]
res = solution.moveZeroes(nums)
print(nums)
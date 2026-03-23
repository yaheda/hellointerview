from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        left = 0
        right = len(nums) - 1
        mid = 0

        while mid <= right:
            if nums[mid] == 0: # move zero to left side
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2: # but don't advance mid because the new nums[mid] needs to be checked
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1

        return

nums = [2,1,2,0,1,0,1,0,1]
solution = Solution()
solution.sortColors(nums)
print(nums)

#You’re pushing 0s to the front, 2s to the back, and letting 1s stay in the middle.
from typing import List


class Solution:

    def __isValid(self, a,b,c):
        valid = a + b > c and a + c > b and b + c > a
        return valid

    def triangleNumber1(self, nums: List[int]) -> int:
        nums.sort()
        # [4,6,9,11,15,18]
        count = 0
        for i in range(len(nums) - 1):
            left = i + 1
            right = i + 2

            # if self.isValid(nums[i], nums[left], nums[right]):
            #     count += 1
            #     right += 1

            # while self.isValid(nums[i], nums[left], nums[right]):
            #     count += 1
            #     right += 1
            
            # left += 1

            while right < len(nums) - 1:
                if self.__isValid(nums[i], nums[left], nums[right]): 
                    count += 1

                if left == right - 1:
                    right += 1
                else:
                    left += 1


        return count
    
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums) - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]: # only check a + b > c because it is sorted -> a > b > c
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count



solution = Solution()
nums = [11,4,9,6,15,18]
res = solution.triangleNumber(nums)
print(res)
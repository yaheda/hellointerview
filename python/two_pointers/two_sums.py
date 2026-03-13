from typing import List


def twoSum(nums: List[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left < right:
        pointer_sum = nums[left] + nums[right];
        print(f"{pointer_sum} = {nums[left]} + {nums[right]}")
        if pointer_sum == target:
            return True
        
        if pointer_sum > target:
            right -= 1
        else:
            left += 1

    return False

nums = [1,3,4,6,8,10,13]
target = 13

nums = [1,3,4,6,8,10,13]
target = 6

print(twoSum(nums, target))
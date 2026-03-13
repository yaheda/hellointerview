from typing import List


def threeSum1(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3: return False

    result = []

    left = 0
    right = 2

    while left < len(nums) - 2 and right < len(nums):
        sum = nums[left] + nums[left + 1] + nums[right]
        print(f"{sum}");
        if sum == 0: 
            result.append([nums[left], nums[left + 1], nums[left + 2]])
            right += 1
        elif left + 1 == right:
            right += 1
        else:
            left += 1

    return result

def threeSum2(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3: return False

    result = []

    left = 0
    right = 2

    pointer1 = 0
    pointer2 = len(nums) - 2
    pointer3 = len(nums) - 1

    go_left = True

    nums.sort()
    print(f"{nums}")
    while pointer1 < pointer3 and (pointer2 != pointer1):
        sum = nums[pointer1] + nums[pointer2] + nums[pointer3]
        print(f"{sum}");
        if sum == 0: 
            result.append([nums[pointer1], nums[pointer2], nums[pointer3]])
        
        
        print(f"pointer 1: {pointer1} : pointer 2: {pointer2} : pointer 3: {pointer3}")

        if go_left == True and pointer1 == (pointer2 - 1):
            go_left = False
            pointer2 += 1
            pointer1 += 1
            continue
        
        if go_left == False and pointer3 == (pointer2 + 1):
            go_left = True
            pointer2 -= 1
            pointer3 -= 1
            continue

        if go_left == True:
            pointer2 -= 1
        else:
            pointer2 += 1
        
        print(f"pointer2 After: {pointer2}")

    return result

def threeSum(nums: List[int]) -> List[List[int]]:
    result = []

    nums.sort()
    for i in range(len(nums) - 1):
        if i > 0 and nums[i] == nums[i - 1]: # we have already checked any combination of that element
            continue

        # init pointers
        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                
                while nums[left] == nums[left - 1] and left < right: # only need to evaluate 1 pointer
                    left += 1

    return result

nums = [-1,0,1,2,-1,-1]
print(threeSum(nums))
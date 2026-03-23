from typing import List


class Solution:
    def trappingWater111(self, height: List[int]) -> int:
        res = 0

        left, right = 0, 1
        mid = 0

        while left < right:
            if left == 0 and height[left] == 0:
                left += 1
                right += 1
            elif right == left + 1:
                if height[right] > height[left]:
                    right += 1
                    left += 1
                else:
                    right += 1
            # elif right == left + 1 and height[right] > height[left]:
            #     right += 1
            #     left += 1
            # elif right == left + 1 and height[right] < height[left]:
            #     #res += height[left] - height[right]
            #     right += 1
            elif height[right] > height[left] or height[right] < height[left]: # can trap water
                if right != len(height) - 1 and height[right] < height[left]:
                    right += 1
                    continue
                
                if right != len(height) - 1 and height[right] >= height[left]:
                    for i in range(left + 1, right):
                        res += height[left] - height[i]
                    left = right
                    right += 1
                    continue

                #if height[right] < height[left]:

                # for i in range(left + 1, right):
                #     res += height[right] - height[i]
                # break
            else:
                right += 1
                #break

        return res
    
    def trappingWater(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        leftMax = height[left]
        rightMax = height[right]

        res = 0

        while left < right:
            if leftMax <= rightMax: # shift left pointer as we only lokking for min and leftMax is smaller
                left += 1
                # can trap zero water here
                potentialWater = leftMax - height[left]
                if potentialWater > 0:
                    res += potentialWater

                if height[left] > leftMax: # update left max if we have a new max at left index
                    leftMax = height[left]
            else:
                right -= 1
                potentialWater = rightMax - height[right] 
                if potentialWater > 0:
                    res += potentialWater

                if height[right] > rightMax:
                    rightMax = height[right]


        return res

solution = Solution()
height = [3, 4, 1, 2, 2, 5, 1, 0, 2]
height = [0,2,0,3,1,0,1,3,2,1]
res = solution.trappingWater(height)
print(res)
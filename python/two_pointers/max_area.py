from typing import List


def max_area(heights: List[int]):
    left, right = 0, len(heights) - 1

    area = 0
    
    while left < right:
        height = heights[left] if heights[left] < heights[right] else heights[right] 
        width = right - left
        pointer_area = height * width
        print(f"{pointer_area} = {height} * {width} from {heights[left]} and {heights[right]}")

        if pointer_area > area:
            area = pointer_area
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -=1
    
    return area


heights = [3, 4, 1, 2, 2, 4, 1, 3, 2]
heights = [1, 2, 1]
result = max_area(heights)
print(result)
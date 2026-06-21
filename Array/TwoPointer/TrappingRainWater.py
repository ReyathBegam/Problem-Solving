# Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

# Examples:

# Input: arr[] = [3, 0, 1, 0, 4, 0, 2]
# Output: 10
# Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.

# Input: arr[] = [3, 0, 2, 0, 4]
# Output: 7
# Explanation: Total water trapped = 0 + 3 + 1 + 3 + 0 = 7 units.
# Input: arr[] = [1, 2, 3, 4]
# Output: 0
# Explanation: We cannot trap water as there is no height bound on both sides.
# Input: arr[] = [2, 1, 5, 3, 1, 0, 4]
# Output: 9
# Explanation: Total water trapped = 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units.
# Constraints:
# 1 < arr.size() < 105
# 0 < arr[i] < 103

class WaterTrapping:
    def maxWater(self, arr):
        # code here
        water=0
        left=0
        right=len(arr)-1
        lmax=0
        rmax=0
        while left<right:
            lmax=max(lmax,arr[left])
            rmax=max(rmax,arr[right])
            if arr[left]<=arr[right]:
                water+=lmax-arr[left]
                left+=1
            else:
                water+=rmax-arr[right]
                right-=1
        return water
print(WaterTrapping().maxWater([3, 0, 1, 0, 4, 0, 2]))
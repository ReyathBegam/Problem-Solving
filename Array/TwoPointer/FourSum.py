# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
 

# Constraints:

# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109
 

class Four(object):
    def fourSum(self, nums, target):
        r = set()
        nums.sort()

        for i in range(len(nums) - 3):

            for j in range(i + 1, len(nums) - 2):

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    curr = nums[i] + nums[j] + nums[left] + nums[right]

                    if curr == target:
                        r.add((
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ))

                        left += 1
                        right -= 1

                    elif curr < target:
                        left += 1

                    else:
                        right -= 1

        return [list(x) for x in r]
    
print(Four().fourSum([1,0,-1,0,-2,2], 0))
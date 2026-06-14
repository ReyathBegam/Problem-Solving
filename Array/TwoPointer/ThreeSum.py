# Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.

# Return true if such a triplet exists, otherwise, return false.

# Examples: 

# Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
# Output: true 
# Explanation: The triplet {1, 4, 8} sums up to 13.
# Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10
# Output: true 
# Explanation: The triplets {1, 3, 6} and {1, 2, 7} both sum to 10. 
# Input: arr[] = [40, 20, 10, 3, 6, 7], target = 24
# Output: false 
# Explanation: No triplet in the array sums to 24.
# Constraints:
# 3 ≤ arr.size() ≤ 5*103
# 0 ≤ arr[i], target ≤ 105

class Three:
    def hasTripletSum(self, arr, target):
        # Code Here
        arr.sort()
        for i in range(len(arr)-2):
            left=i+1
            right=len(arr)-1
            while left<right:
                curr=arr[i]+arr[left]+arr[right]
                if curr==target:
                    return True
                elif curr<target:
                    left+=1
                else:
                    right-=1
        return False
print(Three().hasTripletSum([1, 4, 45, 6, 10, 8], 13))
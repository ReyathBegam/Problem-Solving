# Given an array arr[] of integers, determine whether it contains a triplet whose sum equals zero. Return true if such a triplet exists, otherwise, return false.

# Examples:

# Input: arr[] = [0, -1, 2, -3, 1]
# Output: true
# Explanation: The triplet [0, -1, 1] has a sum equal to zero.
# Input: arr[] = [1, 2, 3]
# Output: false
# Explanation: No triplet with a sum of zero exists.
# Input: arr[] = [-5, 3, 2, -1, 0, 1]
# Output: true
# Explanation: The triplet [-5, 3, 2] has a sum equal to zero.
# Constraints:
# 1 ≤ arr.size() ≤ 103
# -106 ≤ arr[i] ≤ 106

class Triplet:
    def findTriplets(self, arr):
        #code here
        arr.sort()
        for i in range(len(arr)-2):
            left=i+1
            right=len(arr)-1
            while left<right:
                curr=arr[i]+arr[left]+arr[right]
                if curr==0:
                    return True
                elif curr<0:
                    left+=1
                else:
                    right-=1
        return False
    
print(Triplet().findTriplets([0, -1, 2, -3, 1]))
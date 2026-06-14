# Given an array arr[], count the number of distinct triplets (a, b, c) such that:

# a + b = c

# Each triplet is counted only once, regardless of the order of a and b.

# Examples:

# Input: arr[] = [1, 5, 3, 2]
# Output: 2 
# Explanation: There are 2 triplets: 1 + 2 = 3 and 3 +2 = 5
# Input: arr[] = [2, 3, 4]
# Output: 0
# Explanation: No such triplet exits in the given array.
# Input: arr[] = [1, 2, 1, 1]
# Output: 1
# Explanation: Since we need to consider only distinct, we have only one triplet (1, 1, 2).
# Constraints:
# 1 ≤ arr.size() ≤ 103
# 1 ≤ arr[i] ≤ 105

class Triplet:
    def countTriplet(self, arr):
        arr.sort()
        r = set()
        n = len(arr)
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                curr = arr[left] + arr[right]
                if curr == arr[i]:
                    r.add((arr[left], arr[right], arr[i]))
                    left += 1
                    right -= 1
                elif curr < arr[i]:
                    left += 1
                else:
                    right -= 1
        return len(r)
print(Triplet().countTriplet([1, 5, 3, 2]))
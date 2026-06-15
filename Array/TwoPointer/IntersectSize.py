# Given two unsorted integer arrays a[] and b[] each consisting of distinct elements, the task is to return the count of elements in the intersection (or common elements) of the two arrays.

# Intersection of two arrays can be defined as the set containing distinct common elements between the two arrays. 

# Examples:

# Input: a[] = [89, 24, 75, 11, 23], b[] = [89, 2, 4]
# Output: 1
# Explanation: 89 is the only element in the intersection of two arrays.
# Input: a[] = [1, 2, 4, 3, 5, 6], b[] = [3, 4, 5, 6, 7]
# Output: 4
# Explanation: 3, 4, 5, and 6 are the elements in the intersection of two arrays.
# Input: a[] = [20, 10, 30, 50, 40], b[] = [15, 25, 30, 20, 35]
# Output: 2
# Explanation: 20 and 30 are the elements in the intersection of the two arrays.
# Constraints:
# 1  ≤  a.size(), b.size() ≤  105
# 1  ≤  a[i], b[i]  ≤  105


class Inter:
    def intersectSize(self,a, b):
        # code here
        a.sort()
        b.sort()
        c=[]
        i=0
        j=0
        while i<len(a) and j<len(b):
            if a[i]==b[j]:
                c.append(i)
                i+=1
                j+=1
            elif a[i]<b[j]:
                i+=1
            else:
                j+=1
        return len(c)
print(Inter().intersectSize([89, 24, 75, 11, 23], [89, 2, 4]))
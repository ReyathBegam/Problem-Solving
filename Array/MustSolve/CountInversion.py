# Given an array of integers arr[]. You have to find the Inversion Count of the array. 
# Note : Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].

# Examples:

# Input: arr[] = [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
# Input: arr[] = [2, 3, 4, 5, 6]
# Output: 0
# Explanation: As the sequence is already sorted so there is no inversion count.
# Input: arr[] = [10, 10, 10]
# Output: 0
# Explanation: As all the elements of array are same, so there is no inversion count.
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 104

class countinversion:
    def merge(self,arr,low,mid,high):
        temp=[]
        left=low
        right=mid+1
        count=0
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                count+=(mid-left+1)
                right+=1
        while left<=mid:
            temp.append(arr[left])
            left+=1
        while right<=high:
            temp.append(arr[right])
            right+=1
        for i in range(low,high+1):
            arr[i]=temp[i-low]
        return count
    def mergesort(self,arr,low,high):
        
        if low>=high:
            return 0
        count=0
        mid=(low+high)//2
        count+=self.mergesort(arr,low,mid)
        count+=self.mergesort(arr,mid+1,high)
        count+=self.merge(arr,low,mid,high)
        return count
    def inversionCount(self, arr):
        # Code Here
        return self.mergesort(arr,0,len(arr)-1)

print(countinversion().inversionCount([2, 4, 1, 3, 5]))
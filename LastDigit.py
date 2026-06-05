# You are given two integers a and b in the form of strings. You need to find the last digit of ab.

# Examples:

# Input: a = "3", b = "10"
# Output: 9
# Explanation: 310 = 59049. Last digit is 9.
# Input: a = "6", b = "2"
# Output: 6
# Explanation: 62 = 36. Last digit is 6.
# Constraints:
# 1 ≤ a.size(), b.size() ≤ 1000

class Solution:
    def getLastDigit(selff,a, b):
        # code here
          return pow(int(a),int(b),10)
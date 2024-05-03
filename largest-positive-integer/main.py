class Solution(object):
    def findMaxK(self, nums):
        largest_value = -1
        hashMap = {}

        for num in nums:
            if abs(num) in hashMap:
                if abs(num) > largest_value and num / abs(num) != hashMap[abs(num)]:
                    largest_value = abs(num)
            else:
                hashMap[abs(num)] = num / abs(num)

        return largest_value

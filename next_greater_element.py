class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = [-1] * len(nums1)
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]), len(nums2)):
                if nums2[j] > nums1[i]:
                    result[i] = nums2[j]
                    break
        
        return result
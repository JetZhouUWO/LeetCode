class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1,n2,rst = 0,0,[]
        nums1,nums2=sorted(nums1),sorted(nums2)
        while n1<len(nums1) and n2<len(nums2):
            if nums1[n1] < nums2[n2]:
                n1+=1
            elif nums1[n1] > nums2[n2]:
                n2+=1
            else:
                rst.append(nums1[n1])
                n1+=1
                n2+=1
        return rst
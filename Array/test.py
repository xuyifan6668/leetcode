class Solution:
    def merge(self, nums1: list[int], m:int, nums2: list[int], n:int) -> None:
        if nums1[-1] == 0:
            nums1 = nums2
            print(nums1)
        elif n != 0:
            for i in range(m):
                if nums1[i] > nums2[0]:
                    temp = nums1[i]
                    nums1[i] = nums2[0]
                    nums2[0] = temp
                    for j in range(n-1):
                        if nums2[j] > nums2[j + 1]:
                            temp = nums2[j]
                            nums2[j] = nums2[j + 1]
                            nums2[j + 1] = temp
                        else:
                            break
            for k in range(n):
                nums1[m + k] = nums2[k]

class Solution2:
    def merge(self, nums1: list[int], m:int, nums2: list[int], n:int) -> None:
        index1 = m-1
        index2 = n-1
        index = m+n-1
        while (index1 >= 0) & (index2 >= 0):
            if nums1[index1] >= nums2[index2]:
                nums1[index] = nums1[index1]
                index1-=1
            else:
                nums1[index] = nums2[index2]
                index2-=1
            index-=1

if __name__ == "__main__":
    solution = Solution2()
    solution.merge(nums1=[0], m=0, nums2=[1], n=1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # for num in nums2:
        #     nums1.remove(0)
        #     nums1.append(num)

        for num in range(n):
            nums1.append(nums2[num])
            nums1.remove(0)

        total_length = m+n
        for i in range(total_length-1):
            print(f'pass : {i}')
            for j in range(total_length-i-1):
                # swapped = False
                print(f'nums1 is {nums1}')
                print(f'nums1[j] is {nums1[j]}')
                print(f'nums1[j+1] is {nums1[j+1]}')
                if nums1[j] > nums1[j+1]:
                    nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
                    # swapped = True

            # if not swapped:
            #     break

        return nums1


nums1 = [0, 0, 3, 0, 0, 0, 0, 0, 0]
m = 3
nums2 = [-1, 1, 1, 1, 2, 3]
n = 6

solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)

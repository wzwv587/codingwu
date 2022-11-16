"""
二分法适用条件：1.有序数组 2. 数组中无重复元素
注意事项：区间的定义一般为两种，左闭右闭即[left, right]，或者左闭右开即[left, right)
"""
#####此方法为左闭右闭[]####
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 #定义target在左闭右闭的区间里，[left, right]
        
        while left <= right:
            middle = (left + right) // 2 

            if nums[middle] < target:
                left = middle + 1 #target 在右区间，所以[middle + 1, right]
            elif nums[middle] > target:
                right = middle - 1 # target 在左区间，所以[left, middle - 1]
            else:
                return middle #找到目标值
        return -1 # 未找到


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) #定义target在左闭右开的区间里，[left, right)

        while left < right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1 #target 在右区间，所以[middle + 1, right)
            elif nums[middle] > target:
                right = middle #target 在左区间，所以[left, middle)
            else:
                return middle # 找到目标
        return -1 # 未找到目标


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None or len(nums)==0: 
            return 0 
        l=0
        r=len(nums)-1
        while l<r: 
            while(l<r and nums[l]!=val):
                l+=1
            while(l<r and nums[r]==val):
                r-=1
            nums[l], nums[r]=nums[r], nums[l]
        print(nums)
        if nums[l]==val: 
            return l 
        else: 
            return l+1
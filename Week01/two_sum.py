class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=set()
        le=len(nums)
        for i in range(le):
            if target-nums[i] in a:#判断（目标值-新遍历的元素）是否存在集合内元素与之相同
                return [i,nums.index(target-nums[i])]#返回新遍历的元素索引，index获得另外一个元素索引
            a.add(nums[i])#将遍历的列表元素存入集合
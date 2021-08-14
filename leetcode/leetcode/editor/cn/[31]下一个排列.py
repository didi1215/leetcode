# 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。 
# 
#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。 
# 
#  必须 原地 修改，只允许使用额外常数空间。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 100 
#  
#  Related Topics 数组 双指针 
#  👍 1271 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 将一个左边的「较小数」与一个右边的「较大数」交换，以能够让当前排列变大，从而得到下一个排列。
        # 同时我们要让这个「较小数」尽量靠右，而「较大数」尽可能小。当交换完成后,「较大数」右边的数需要按照升序重新排列。这样可以在保证新排列大于原来排列的情况下，使变大的幅度尽可能小。
        i = len(nums) - 2
        # 1.首先从后向前查找第一个顺序对(i,i+1)，满足a[i]<a[i+1]。较小数为a[i],[i+1,n)必然是下降序列
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # 2.如果找到了顺序对，那么在[i+1,n)中从后向前查找第一个元素j满足a[i]<a[j],较大数即为a[j]
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
                # 3.交换a[i],[j]，此时可证明[i+1,n)为降序，可以直接使用双指针反转区间使其变为升序，而无需排序
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        # 如果在步骤1找不到顺序对，说明当前序列已经是一个降序序列，即最大的序列，我们直接跳过步骤2执行步骤3，即可得到最小的升序序列。
# leetcode submit region end(Prohibit modification and deletion)

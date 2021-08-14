# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [3,4,3,3]
# 输出：4
#  
# 
#  示例 2： 
# 
#  输入：nums = [9,1,7,9,7,9,7]
# 输出：1 
# 
#  
# 
#  限制： 
# 
#  
#  1 <= nums.length <= 10000 
#  1 <= nums[i] < 2^31 
#  
# 
#  
#  Related Topics 位运算 数组 
#  👍 215 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] = False
            else:
                dic[num] = True
        for c in dic:
            if dic[c]:
                return c
# leetcode submit region end(Prohibit modification and deletion)

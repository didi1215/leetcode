# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。 
# 
#  示例: 
# 
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7 
# 
#  
# 
#  提示： 
# 
#  你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。 
# 
#  注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/ 
#  Related Topics 队列 滑动窗口 单调队列 堆（优先队列） 
#  👍 302 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        n = len(nums)
        res = []
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 删除queue中对应的nums[i-1]
            if i > 0 and queue[0] == nums[i - 1]:
                queue.popleft()
            # 保持queue递减
            while queue and queue[-1] < nums[j]:
                queue.pop()
            queue.append(nums[j])
            # 记录窗口最大值
            if i >= 0:
                res.append(queue[0])
        return res
# leetcode submit region end(Prohibit modification and deletion)

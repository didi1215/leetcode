# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一
# 格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但
# 它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？ 
# 
#  
# 
#  示例 1： 
# 
#  输入：m = 2, n = 3, k = 1
# 输出：3
#  
# 
#  示例 2： 
# 
#  输入：m = 3, n = 1, k = 0
# 输出：1
#  
# 
#  提示： 
# 
#  
#  1 <= n,m <= 100 
#  0 <= k <= 20 
#  
#  Related Topics 深度优先搜索 广度优先搜索 动态规划 
#  👍 328 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    # 由于题目要求从 (0, 0) 点出发，因此任何一个点都可以只通过向右和向下两个动作达到，因此代码中可以只考虑这两个方向。
    def movingCount(self, m: int, n: int, k: int) -> int:
        def getDigitSum(num):
            ans = 0
            while num:
                ans += num % 10
                num //= 10
            return ans

        # 广度优先搜索
        marked = set()
        queue = collections.deque()  # deque是双向队列
        queue.append((0, 0))
        while queue:
            x, y = queue.popleft()  # pop队首
            if (x, y) not in marked and getDigitSum(x) + getDigitSum(y) <= k:
                marked.add((x, y))
                for dx, dy in [(1, 0), (0, 1)]:  # 仅考虑向右和向下
                    if 0 <= x + dx < m and 0 <= y + dy < n:
                        queue.append((x + dx, y + dy))
        return len(marked)
# leetcode submit region end(Prohibit modification and deletion)

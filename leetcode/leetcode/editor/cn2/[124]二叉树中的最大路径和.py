# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不
# 一定经过根节点。 
# 
#  路径和 是路径中各节点值的总和。 
# 
#  给你一个二叉树的根节点 root ，返回其 最大路径和 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6 
# 
#  示例 2： 
# 
#  
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目范围是 [1, 3 * 104] 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics 树 深度优先搜索 动态规划 二叉树 
#  👍 1131 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):  # 定义一个类内部可用的私有初始化变量
        self.maxSum = float("-inf")
        # inf正无穷，-inf负无穷

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0
            # 递归定义左子树和右子树的最大路径，<0的舍弃
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            # 新的路径值=左子树路径值+右子树路径值+根节点值
            pricenewpath = leftGain + rightGain + node.val
            # 最大和=最大和和新的路径值中取最大值
            self.maxSum = max(pricenewpath, self.maxSum)
            # 非叶子节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum
# leetcode submit region end(Prohibit modification and deletion)

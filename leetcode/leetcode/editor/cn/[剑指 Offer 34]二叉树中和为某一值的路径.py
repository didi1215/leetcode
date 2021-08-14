# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。 
# 
#  
# 
#  示例: 
# 给定如下二叉树，以及目标和 target = 22， 
# 
#  
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#  
# 
#  返回: 
# 
#  
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 10000 
#  
# 
#  注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/ 
#  Related Topics 树 深度优先搜索 回溯 二叉树 
#  👍 218 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        # 回溯法:先序遍历+路径记录
        res, path = [], []

        def recur(root, tar):
            # 当前节点root，当前目标值tar
            # 终止条件；root为空返回
            if not root:
                return
            # 递推
            # 1.路径更新：当前节点root.val加入path
            path.append(root.val)
            # 2.目标值更新：tar = tar - root.val
            tar -= root.val
            # 3.路径记录：当root为叶节点且和等于目标值，则该path加入res
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
                # 值得注意的是，记录路径时若直接执行res.append(path),则是将path对象加入了res,后续path改变时,res中的path对象也会随之改变
                # 正确做法：res.append(list(path)) ，相当于复制了一个 path 并加入到 res
            # 4.先序遍历，递归左右子节点
            recur(root.left, tar)
            recur(root.right, tar)
            # 5.路径恢复：向上回溯前，需要将当前节点从path中删除，即pop
            path.pop()

        recur(root, target)
        return res
# leetcode submit region end(Prohibit modification and deletion)

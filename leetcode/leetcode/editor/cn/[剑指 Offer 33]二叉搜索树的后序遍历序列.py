# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。 
# 
#  
# 
#  参考以下这颗二叉搜索树： 
# 
#       5
#     / \
#    2   6
#   / \
#  1   3 
# 
#  示例 1： 
# 
#  输入: [1,6,3,2,5]
# 输出: false 
# 
#  示例 2： 
# 
#  输入: [1,3,2,6,5]
# 输出: true 
# 
#  
# 
#  提示： 
# 
#  
#  数组长度 <= 1000 
#  
#  Related Topics 栈 树 二叉搜索树 递归 二叉树 单调栈 
#  👍 321 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            # 终止条件：当i>=j，说明此子树节点数量<=1，无需判别正确性，直接返回true
            if i >= j:
                return True
            # 递推工作
            # 1.划分左右子树，遍历后序遍历的[i,j]区间元素，寻找第一个大于根节点的节点，索引记为m
            # 左子树[i,m-1] 右子树[m,j]
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            # 2.判断是否为二叉搜索树
            # 左子树区间内所有节点都应该小于postorder[j]，1步骤已经完成了
            # 右子树区间内所有节点都应该大于postorder[j],当遇到<=就跳出
            while postorder[p] > postorder[j]:
                p += 1

            # 返回值：所有子树都要正确，因此用&&连接
            # 1.p==j判断此树
            # 2.recur(i,m-1)
            # 3.recur(m,j-1)
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)
# leetcode submit region end(Prohibit modification and deletion)

# 请实现两个函数，分别用来序列化和反序列化二叉树。 
# 
#  你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字
# 符串反序列化为原始的树结构。 
# 
#  提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方
# 法解决这个问题。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
#  
# 
#  
# 
#  注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-b
# inary-tree/ 
#  Related Topics 树 深度优先搜索 广度优先搜索 设计 字符串 二叉树 
#  👍 227 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Codec:
    # 层序遍历
    # 递推公式：列表[0,n]，m为null个数
    # node.val == null时 索引: node->n, node.left->2(n-m)+1, node.right->2(n-m)+2
    # node.val != null时 索引: node->n, 无, 无
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 特例处理: 若root为空，直接返回空列表[]
        if not root:
            return '[]'
        # 初始化: 队列queue；列表res
        queue = collections.deque()
        queue.append(root)  # 要初始化queue，加入root
        res = []
        # 层序遍历: 当queue为空时跳出
        while queue:
            # 1.节点出队，记为node
            node = queue.popleft()
            # 2.若node不为空（1）打印node.val (2)左右节点加入queue
            if node:
                res.append(str(node.val))  # 注意变量类型
                queue.append(node.left)
                queue.append(node.right)
            # 3.若node为空，打印'null'
            else:
                res.append('null')
        # 拼接列表，','隔开，首尾加[]
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 特例处理：data为空则返回null
        if data == '[]':
            return
        # 初始化：序列化列表vals:先去掉首尾[],再用,隔开指针i=1,根节点为root(vals[0]),队列queue(包含root)
        vals = data[1:-1].split(',')
        # 错误写法root = vals[0]
        root = TreeNode(int(vals[0]))  # 要初始化queue，加入root
        i = 1
        queue = collections.deque()
        queue.append(root)
        # 按层构建：queue为空时跳出
        while queue:
            # 1.节点出队记为node
            node = queue.popleft()
            # 2.node.left = vals[i],入栈
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))  # 注意变量类型
                queue.append(node.left)
            # 3.i+=1
            i += 1
            # 4.node.right = vals[i],入栈
            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            # 5.i+=1
            i += 1
        # 返回根节点root即可
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)

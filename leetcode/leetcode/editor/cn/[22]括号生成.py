# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics 字符串 动态规划 回溯 
#  👍 1954 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []

        # 增加了left与right参数，分别代表左括号与右括号的数量，每生成一个我就增加一个
        def dfs(path, left, right):
            # 结束DFS的条件首先就需要把不符合的给过滤掉
            if left > n or right > left:
                return
            if len(path) == 2 * n:
                res.append(path)
                return
            dfs(path + '(', left + 1, right)
            dfs(path + ')', left, right + 1)

        res = []
        dfs('', 0, 0)
        return res
# leetcode submit region end(Prohibit modification and deletion)

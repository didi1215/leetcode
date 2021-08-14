# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。 
# 
#  示例 1: 
# 
#  输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]
#  
# 
#  
# 
#  说明： 
# 
#  
#  用返回一个整数列表来代替打印 
#  n 为正整数 
#  
#  Related Topics 数组 数学 
#  👍 139 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        #        大数问题
        # 全排列解法
        def dfs(index, num, digit):
            if index == digit:
                res.append(int(''.join(num)))
                return
            for i in range(10):
                num.append(str(i))
                dfs(index + 1, num, digit)
                num.pop()

        res = []
        for digit in range(1, n + 1):
            for first in range(1, 10):
                num = [str(first)]
                dfs(1, num, digit)
        return res
# leetcode submit region end(Prohibit modification and deletion)

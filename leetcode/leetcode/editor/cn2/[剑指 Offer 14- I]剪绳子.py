# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
# 请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18
# 。 
# 
#  示例 1： 
# 
#  输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1 
# 
#  示例 2: 
# 
#  输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36 
# 
#  提示： 
# 
#  
#  2 <= n <= 58 
#  
# 
#  注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/ 
#  Related Topics 数学 动态规划 
#  👍 279 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def cuttingRope(self, n: int) -> int:
        # n = n1+n2+n3+...na求max(n1,n2,n3,...na)数学问题
        # n<=3时，按照规则不应切分但是必须切m>1段，因此必须剪出一段长为1的绳子，即返回n-1
        # 当n>3时，n=3a+b
        # b=0 return 3**a
        # b=1 return 3**(a-1)*2*2
        # b=2 return 3**a*2
        if n <= 3:
            return n - 1
        a = n // 3
        b = n % 3
        if b == 0:
            return 3 ** a
        elif b == 1:
            return 3 ** (a - 1) * 4
        else:
            return 3 ** a * 2
# leetcode submit region end(Prohibit modification and deletion)

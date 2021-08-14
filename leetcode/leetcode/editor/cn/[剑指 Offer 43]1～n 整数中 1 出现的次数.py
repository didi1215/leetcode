# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。 
# 
#  例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 12
# 输出：5
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 13
# 输出：6 
# 
#  
# 
#  限制： 
# 
#  
#  1 <= n < 2^31 
#  
# 
#  注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/ 
#  Related Topics 递归 数学 动态规划 
#  👍 214 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDigitOne(self, n: int) -> int:
        # 设n为x位数，当前位ni记为cur，i-1 -> 1记为低位low，x -> i+1记为高位high，10^x记为位因子digit
        # 初始化
        high = n // 10
        cur = n % 10
        low = 0
        digit = 1
        res = 0
        # 从个位到最高位递推
        # 当 high 和 cur 同时为 0 时，说明已经越过最高位
        while high != 0 or cur != 0:
            # cur=0时，此位1出现次数=high*digit
            if cur == 0:
                res += high * digit
            # cur=1时，high*digit+low+1
            elif cur == 1:
                res += high * digit + low + 1
            # cur=2-9时，(high+1)*digit
            else:
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res
# leetcode submit region end(Prohibit modification and deletion)

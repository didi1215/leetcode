# 数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，
# 等等。 
# 
#  请写一个函数，求任意第n位对应的数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 3
# 输出：3
#  
# 
#  示例 2： 
# 
#  输入：n = 11
# 输出：0 
# 
#  
# 
#  限制： 
# 
#  
#  0 <= n < 2^31 
#  
# 
#  注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/ 
#  Related Topics 数学 二分查找 
#  👍 157 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNthDigit(self, n: int) -> int:
        # 数位n 数字num 位数digit 梅digit位数的起始数字(1,10,100,...)记为start
        # 位数digit = digit + 1
        # start = start * 10
        # count = 9 * start * digit
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        # 所求数位在从数字start开始的第[(n-1)/digit]个数字中
        num = start + (n - 1) // digit
        s = str(num)
        # 所求数位在num的第(n-1)%digit位
        res = int(s[(n - 1) % digit])
        return res
# leetcode submit region end(Prohibit modification and deletion)

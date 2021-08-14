# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,5,6,4]
# 输出: 5 
# 
#  
# 
#  限制： 
# 
#  0 <= 数组长度 <= 50000 
#  Related Topics 树状数组 线段树 数组 二分查找 分治 有序集合 归并排序 
#  👍 497 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 归并排序+逆序对统计
        def merge_sort(l, r):
            # 终止条件：l>=r代表子数组长度为1，此时终止划分
            if l >= r:
                return 0
            # 递归划分：求中点m，递归左子数组，右子数组
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            # 合并与逆序对统计
            # 1.暂存nums[l,r]至辅助数组tmp
            # 2.循环合并
            i, j = l, m + 1
            tmp[l:r + 1] = nums[l:r + 1]
            for k in range(l, r + 1):
                # 左子树已合并完
                if i == m + 1:
                    nums[k] = tmp[j]
                    j += 1
                # 右子树已合并完
                elif j == r + 1:
                    nums[k] = tmp[i]
                    i += 1
                # 左子数组当前元素更小
                elif tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                # 右子数组当前元素更小
                else:
                    nums[k] = tmp[j]
                    j += 1
                    res += m - i + 1
            return res

        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1)

# leetcode submit region end(Prohibit modification and deletion)

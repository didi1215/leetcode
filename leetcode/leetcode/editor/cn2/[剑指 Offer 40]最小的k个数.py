# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#  
# 
#  示例 2： 
# 
#  输入：arr = [0,1,2,1], k = 1
# 输出：[0] 
# 
#  
# 
#  限制： 
# 
#  
#  0 <= k <= arr.length <= 10000 
#  0 <= arr[i] <= 10000 
#  
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列） 
#  👍 276 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quick_sort(arr, l, r):
            # 子数组长度为 1 时终止递归
            if l >= r: return
            # 哨兵划分操作（以 arr[l] 作为基准数）
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]: j -= 1
                while i < j and arr[i] <= arr[l]: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            # 递归左（右）子数组执行哨兵划分
            quick_sort(arr, l, i - 1)
            quick_sort(arr, i + 1, r)

        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]
# leetcode submit region end(Prohibit modification and deletion)

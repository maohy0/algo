def min_subarray(nums, s) -> int:
    # 采用滑动窗口法求解，思想类似1.2用到的双指针
    left = 0 # 左指针
    right = 0 # 右指针
    min_len = float('inf') # 最小子数组长度，初始化为无穷大
    c_sum = 0 # 累计和
    while right < len(nums):
        c_sum += nums[right] # 累加窗口内的数
        while c_sum >= s: # 当累计和大于等于s时，左指针右移，来缩小长度
            min_len = min(min_len, right - left + 1) # 更新最小子数组长度，如果前面的值更小，会被保留
            c_sum -= nums[left] # 要减掉左指针指向的数，因为下一步左指针右移了，对应的数不在窗口内
            left += 1 # 左指针右移

        right += 1 # 右指针右移
    return min_len if min_len != float('inf') else 0 # 如果最小子数组长度为无穷大，则返回0

nums = list(map(int, input("Please input array:\n").split()))
s = int(input("Please input s:\n"))
print(f"Minimum subarray length: {min_subarray(nums, s)}")
from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 定义target在左闭右闭的区间里，[left, right]

    while left <= right:
        middle = left + (right - left) // 2
        
        if nums[middle] > target:
            right = middle - 1  # target在左区间，所以[left, middle - 1]
        elif nums[middle] < target:
            left = middle + 1  # target在右区间，所以[middle + 1, right]
        else:
            return middle  # 数组中找到目标值，直接返回下标
    return -1  # 未找到目标值

# 输入处理
nums = list(map(int, input("请输入一个升序排列的整数数组，用空格分隔:").split()))

target = int(input("请输入要查找的目标值:"))
    
# 调用二分查找
result = search(nums, target)
    
# 输出结果
if result != -1:
    print(f"目标值 {target} 在数组中的索引是: {result}")
else:
    print(f"数组中没有找到目标值 {target}")
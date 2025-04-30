def squared_sorted_array(nums) -> list[int]:
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    nums.sort() # 暴力排序
    return nums

nums = list(map(int, input("Please input array:\n").split()))
print(f"Sorted and Squared array: {squared_sorted_array(nums)}")
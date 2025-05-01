def remove_element(nums: list[int], val: int) -> list[int]:
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return nums[:slow]  # 切片，不需要考虑数组中超出新长度后面的元素

nums = list(map(int, input("请输入数组元素，用空格分隔：").split()))
val = int(input("请输入要删除的元素："))

nums = remove_element(nums, val)
print(f"删除元素后的数组为{nums}，数组长度为{len(nums)}")
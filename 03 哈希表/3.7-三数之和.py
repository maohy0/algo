def sum3(nums: list[int]) -> list[list[int]]:
    # 使用双指针法，较易于理解
    result = []
    nums.sort()

    # 找 a + b + c = 0，3个数
    for i in range(len(nums)):
        if nums[i] > 0:
            return result   # i在最左边，对应a，最小的元素大于0，就不用接着算了
        if i > 0 and nums[i] == nums[i - 1]:
            continue    # 去重

        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])

            # 去重，跟前面a对应一样，b和c分别对应left和right
            while right > left and nums[right] == nums[right - 1]:
                right -= 1
            while right > left and nums[left] == nums[left + 1]:
                left += 1
            
            # 别忘了append之后移动指针，以便下一次迭代
            right -= 1
            left += 1

    return result
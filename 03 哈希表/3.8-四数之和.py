def sum4(nums: list[int], target: int) -> list[list[int]]:
    result = []
    # 类似的，还是双指针
    nums.sort()

    # 找 a + b + c + d = target 4个数
    for i in range(len(nums)):
        # 剪枝，nums[i]大于target大于0了，那么再算下去只会越加越大
        if nums[i] > target and target > 0 and nums[i] > 0:
            break
        # 去重
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] > target and target > 0:
                break
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[j] + nums[left] + nums[right] == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                
                    # 去重
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 如果没有重复也别忘了移动指针，进行下一次循环
                    left += 1
                    right -= 1
                elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

    return result
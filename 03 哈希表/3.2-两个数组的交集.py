if 0:
    def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
        hash_table = {} # 字典，用哈希表存储一个数组中的所有元素
        for num in nums1:
            hash_table[num] = hash_table.get(num, 0) + 1    # 显示第num个元素值，没有显示0，然后把这个值加1，可以理解为，记录num出现的次数
        
        res = set() # 使用集合存储结果
        for num in nums2:
            if num in hash_table:
                res.add(num)
                del hash_table[num]

        return list(res)
elif 0:
    def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
        count1 = [0] * 1001
        count2 = [0] * 1001
        result = [] # 用数组来记录
        for i in range(len(nums1)):
            count1[nums1[i]] += 1   # 记录nums1[i]元素出现的次数
        for j in range(len(nums2)):
            count2[nums2[j]] += 1
        for k in range(1001):
            if count1[k] * count2[k] > 0:
                result.append(k)
        return result
elif 0:
    def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))    # 转成集合来算
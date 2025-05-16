def twosum(nums: list[int], target: int) -> list[int]:
    records = dict()    # 用字典，key-value结构

    # enumerate枚举，同时获取数组中元素的索引和值
    for index, value in enumerate(nums):
        if target - value in records:
            return [records[target - value], index]
        records[value] = index  # 这里注意不要弄反了，key是value，value是index

    return []
def foursumcount(A: list[int], B: list[int], C: list[int], D: list[int]) -> int:
    # 还用字典，注意in 字典判断的是键key
    hashmap = dict()
    for na in A:
        for nb in B:
            if na + nb in hashmap:
                hashmap[na + nb] += 1   # 记的是次数
            else:
                hashmap[na + nb] = 1
    
    result = 0
    for nc in C:
        for nd in D:
            key = - nc - nd
            if key in hashmap:
                result += hashmap[key]
    
    return result

print(foursumcount([1, 2], [-2, -1], [-1, 2], [0, 2]))
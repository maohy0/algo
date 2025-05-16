# 子集问题
def canConstruct(ransom: str, magazines: str) -> bool:
    ransom_record = [0] * 26   # 只有小写字母
    magazines_record = [0] * 26
    for c in ransom:
        ransom_record[ord(c) - ord("a")] += 1
    for c in magazines:
        magazines_record[ord(c) - ord("a")] += 1
    
    # 每个数组的26个元素分别对应字母a-z出现次数，如果ransom的每个字母的出现次数都不多于magazines的，那就说明ransom可以由magazines里面的字符构成
    return all(ransom_record[i] <= magazines_record[i] for i in range(26))

print(canConstruct("aa", "aba"))
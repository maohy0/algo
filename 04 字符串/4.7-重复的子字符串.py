def repeatedSubstring(s: str) -> bool:
    n = len(s)
    if n <= 1:
        return False
    
    ss = s[1:] + s[:-1] # 从元素1开始到结束，再从元素0到倒数第2个，即去掉首字符和尾字符，切片遵循左闭右开区间，如果是一个子串重复多次构成，那应该能拼出来

    return ss.find(s) != -1

print(repeatedSubstring("abcabcabcabc"))
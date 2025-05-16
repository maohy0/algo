import time
def isAnagram(s: str, t: str) -> bool:
    record = [0] * 26   # 一共26个小写字母，哈希表只需要26个元素

    # Python的ord函数返回ASCII值
    for i in s:
        record[ord(i) - ord("a")] += 1
    for i in t:
        record[ord(i) - ord("a")] -= 1
    
    for i in range(26):
        if record[i] != 0:
            return False

    return True

start = time.time()

s = "aee"
t = "eae"

print(isAnagram(s, t))

stop = time.time()

print(f"Time used: {stop - start} s")
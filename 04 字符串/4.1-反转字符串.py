if 0:
    def reversestr(s: list[str]) -> list[str]:
        for i in range(len(s) // 2):
            j = len(s) - i - 1
            s[i], s[j] = s[j], s[i]
        return s
elif 0:
    def reversestr(s: list[str]) -> list[str]:
        s[:] = reversed(s)  # 要切片，reversed返回一个反向迭代器对象，不是列表
        return s
elif 0:
    def reversestr(s: list[str]) -> list[str]:
        s[:] = s[::-1]
        return s
elif 0:
    def reversestr(s: list[str]) -> list[str]:
        s.reverse()
        return s
elif 1:
    def reversestr(s: list[int]) -> list[str]:
        s[:] = [s[i] for i in range(len(s) - 1, -1, -1)]
        return s

print(reversestr(["h", "e", "l", "l", "o"]))
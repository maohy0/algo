def reversestr2(s: list[str], k: int) -> list[str]:
    p = 0

    while p < len(s):
        p2 = p + k
        s = s[:p] + s[p: p2][::-1] + s[p2:]
        p += 2 * k

    return s

print(reversestr2("abcdefg", 2))
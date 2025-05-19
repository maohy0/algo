def right_handed(s: str, k: int) -> str:
    s = s[len(s) - k:] + s[:len(s) - k]
    return s

k = int(input())
s = input()

print(right_handed(s, k))
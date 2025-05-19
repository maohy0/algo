def reverseWords(s: str) -> str:
    s = s[::-1] # 反转字符串

    s = " ".join(word[::-1]for word in s.split())   # split分割，split有2个参数，第1个参数为分割字符，默认为所有的空字符（空格、回车和制表符号），第2个为分割次数，默认为一直分割，分割后返回列表
    # join 合并，连接字符串，.之前为分隔符，可以为空，括号为要连接的元素序列
    return s

print(reverseWords("Hello World"))
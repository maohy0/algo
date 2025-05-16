def ishappy(n: int) -> bool:
    record = set()
    while n not in record:
        record.add(n)
        new_num = 0 # 关键字不能做变量名
        for i in str(n):
            new_num += int(i) ** 2  # i此时是字符形式，要用int转回来
        if new_num == 1:
            return True
        else:
            n = new_num # 更新n的值，以进行下一次循环
    return False

print(ishappy(38))
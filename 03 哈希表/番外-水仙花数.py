# 跟快乐数不同，水仙花数的判断不需要循环，可以一步完成，跟哈希表也没关系，只是写快乐数的时候联想到了复习一下这个非常初级的问题

def is_narcissistic(num: int) -> bool:
    n = len(str(num))   # 位数
    new_sum = 0
    for i in str(num):
        new_sum += int(i) ** n

    if new_sum == num:
        return True
    else:
        return False

print(is_narcissistic(154))
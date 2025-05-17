def generate_matrix(n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]    # 初始化矩阵，n行n列0
    top, bottom, left, right = 0, n-1, 0, n-1   # 初始化上下左右4个边界
    element = 1 # 矩阵元素
    
    while left <= right and top <= bottom:
        for i in range(left, right + 1):    # 注意，python的range是左闭右开区间，默认步长值为1
            matrix[top][i] = element
            element += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = element
            element += 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = element
            element += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            matrix[i][left] = element
            element += 1
        left += 1

    return matrix

print(generate_matrix(3))
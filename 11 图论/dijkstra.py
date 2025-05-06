import sys

def dijkstra(n: int, m: int, edges: list[tuple[int, int, int]], start: int, end: int) -> int:
    # n是节点数，m是边数，edges是边的列表，start是起点编号，end是终点编号
    # 图顶点的编号从1到n+1
    # 初始化邻接矩阵
    graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for p1, p2, val in edges:
        graph[p1][p2] = val # 更新每条边的权重

    # 初始化最短距离数组和访问数组
    min_dist = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)

    min_dist[start] = 0 # 起点到自身的距离为0

    # 遍历所有节点
    for _ in range(n):
        min_val = float('inf')  # 记录当前未访问的节点中最小的距离，初始值为无穷大
        cur = -1

        for j in range(1, n + 1):
            if not visited[j] and min_dist[j] < min_val:
                min_val = min_dist[j]
                cur = j # 找到未访问的节点中距离最小的节点

        if cur == -1: # 如果没有找到未访问的节点，说明所有节点都已经访问过了，直接退出循环
            break

        visited[cur] = True # 标记当前节点为已访问

        # 更新当前节点的邻居节点的距离
        for j in range(1, n + 1):
            if not visited[j] and graph[cur][j] != float('inf') and min_dist[cur] + graph[cur][j] < min_dist[j]:
                min_dist[j] = min_dist[cur] + graph[cur][j] # 更新邻居节点的距离

    return -1 if min_dist[end] == float('inf') else min_dist[end] # 返回终点到起点的最短距离，如果无法到达，返回-1
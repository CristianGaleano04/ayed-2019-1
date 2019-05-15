from sys import stdin


def number_islands(graph):
    def dfs(graph, row, col, visited):
        row_s = len(graph)
        col_s = len(graph[0])
        if row < 0 or row >= row_s or col < 0 or col >= col_s or visited[row][col] or not graph[row][col]:
            return
        visited[row][col] = True
        dfs(graph, row + 1, col, visited)
        dfs(graph, row - 1, col, visited)
        dfs(graph, row, col + 1, visited)
        dfs(graph, row, col - 1, visited)

    if not graph:
        return 0
    rows = len(graph)
    cols = len(graph[0])
    visited_row = [False for c in range(cols)]
    visited = [visited_row[:] for c in range(rows)]
    cont = 0
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] and not visited[i][j]:
                dfs(graph, i, j, visited)
                cont += 1
    return cont


if __name__ == '__main__':
    graph = []
    while True:
        a = [int(c) for c in stdin.readline().strip()]
        if not a:
            break
        graph.append(a)
    print(number_islands(graph))

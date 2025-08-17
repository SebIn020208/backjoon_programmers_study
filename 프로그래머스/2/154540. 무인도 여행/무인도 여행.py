import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    N, M = len(maps), len(maps[0])
    visited = [[False] * M for _ in range(N)]
    
    def dfs(x, y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return 0
        if maps[x][y] == 'X' or visited[x][y]:
            return 0
        
        visited[x][y] = True
        food = int(maps[x][y])
        
        food += dfs(x+1, y)
        food += dfs(x-1, y)
        food += dfs(x, y+1)
        food += dfs(x, y-1)
        
        return food
        
    Island = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] != "X" and not visited[i][j]:
                food = dfs(i, j)
                Island.append(food)
    
    return sorted(Island) if Island else [-1]
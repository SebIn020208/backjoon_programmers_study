# 백준 1516번 골드3 게임개발
from collections import deque

N = int(input())  # 건물 수
graph = [[] for _ in range(N + 1)]  # 건물 그래프
indegree = [0] * (N + 1)  # 진입차수 배열
build_time = [0] * (N + 1)  # 각 건물 기본 건설 시간
result = [0] * (N + 1)  # 각 건물까지 걸리는 최소 시간

for i in range(1, N + 1):
    data = list(map(int, input().split()))
    build_time[i] = data[0]
    for x in data[1:-1]:
        graph[x].append(i)
        indegree[i] += 1

queue = deque()

# 처음에 진입 차수가 0인 건물 -> 바로 건설 가능
# 자기 시간 그대로 기록 result에 저장
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        result[i] = build_time[i]

while queue:
    now = queue.popleft()
    for next in graph[now]:
        indegree[next] -= 1
        # result[next]는 이전의 최대값을 저장해야 함
        result[next] = max(result[next], result[now] + build_time[next])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N + 1):
    print(result[i])


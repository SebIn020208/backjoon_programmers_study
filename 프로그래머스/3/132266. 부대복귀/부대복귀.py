from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    link_road = defaultdict(list)
    for a, b in roads:
        link_road[a].append(b)
        link_road[b].append(a) 

    dist = [-1] * (n+1)  
    dist[destination] = 0

    q = deque([destination])
    while q:
        now = q.popleft()
        for nxt in link_road[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now] + 1
                q.append(nxt)

    return [dist[s] for s in sources]

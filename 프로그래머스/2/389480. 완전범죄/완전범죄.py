def solution(info, n, m):
    answer = float('inf')
    N = len(info)
    visited = set()  # (idx, a_sum, b_sum) 방문 여부 저장

    def dfs(idx, a_sum, b_sum):
        nonlocal answer

        # 경찰에 잡히면 중단
        if a_sum >= n or b_sum >= m:
            return
        # 모든 물건을 다 훔쳤다면 최소값 갱신
        if idx == N:
            answer = min(answer, a_sum)
            return

        # 이미 방문한 상태면 중단
        if (idx, a_sum, b_sum) in visited:
            return
        visited.add((idx, a_sum, b_sum))

        a, b = info[idx]

        # 1️⃣ 이번 물건을 A가 훔치는 경우
        dfs(idx + 1, a_sum + a, b_sum)
        # 2️⃣ 이번 물건을 B가 훔치는 경우
        dfs(idx + 1, a_sum, b_sum + b)

    dfs(0, 0, 0)
    return -1 if answer == float('inf') else answer

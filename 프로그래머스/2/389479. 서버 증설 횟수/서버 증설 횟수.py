def solution(players, m, k):
    answer = 0
    check_p = [0] * len(players)  # 각 시점에 몇 대 증설했는지 기록

    for t, n in enumerate(players):

        # k초 전 증설한 서버 해제
        if t - k >= 0:
            check_p[t - k] = 0

        # 필요한 서버 수 계산
        needed = n // m
        if needed > sum(check_p):
            add = needed - sum(check_p)
            check_p[t] = add
            answer += add

    return answer

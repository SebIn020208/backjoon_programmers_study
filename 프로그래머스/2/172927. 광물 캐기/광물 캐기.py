def solution(picks, minerals):
    # 피로도 테이블: [다이아곡괭이, 철곡괭이, 돌곡괭이]
    fatigue = {
        "diamond": [1, 5, 25],
        "iron":    [1, 1, 5],
        "stone":   [1, 1, 1]
    }

    # 총 곡괭이 개수로 캘 수 있는 최대 광물 수
    max_len = sum(picks) * 5
    minerals = minerals[:max_len]  # 쓸 수 없는 광물은 잘라냄

    # 광물을 5개 단위로 묶어서, 각 곡괭이로 캤을 때 드는 피로도를 계산
    chunks = []
    for i in range(0, len(minerals), 5):
        part = minerals[i:i+5]
        score = [0, 0, 0]  # [다이아, 철, 돌] 곡괭이로 캤을 때 피로도
        for m in part:
            for j in range(3):
                score[j] += fatigue[m][j]
        chunks.append(score)

    # 돌곡괭이로 캤을 때 피로도가 큰 구간부터 좋은 곡괭이 배치
    chunks.sort(key=lambda x: -x[2])

    answer = 0
    for dia, iron, stone in chunks:
        if picks[0] > 0:       # 다이아 곡괭이 있으면
            answer += dia
            picks[0] -= 1
        elif picks[1] > 0:     # 철 곡괭이 있으면
            answer += iron
            picks[1] -= 1
        elif picks[2] > 0:     # 돌 곡괭이 있으면
            answer += stone
            picks[2] -= 1
        else:
            break

    return answer

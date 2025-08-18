def solution(sequence, k):
    n = len(sequence)
    left, right = 0, 0
    curr_sum = sequence[0]
    answer = [0, n-1]  # 기본값: 제일 긴 범위로 초기화

    while left < n and right < n:
        if curr_sum == k:
            # 현재 구간 길이가 기존 답보다 짧으면 갱신
            if (answer[1] - answer[0]) > (right - left):
                answer = [left, right]
            # 합이 맞았으면 왼쪽 이동
            curr_sum -= sequence[left]
            left += 1

        elif curr_sum < k:
            # 오른쪽 확장
            right += 1
            if right < n:
                curr_sum += sequence[right]

        else:  # curr_sum > k
            curr_sum -= sequence[left]
            left += 1

    return answer

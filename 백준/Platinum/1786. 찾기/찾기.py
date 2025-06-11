# 백준 1786번 플래티넘5 찾기

# 문자열 P가 문자열 T 중간에 몇 번, 어느 위치에 나타나는지를 찾는 문제
# P의 길이: m, T의 길이: n

# 비교 도중 매칭에 실패했을 경우를 대비해
# 패턴 P의 접두사와 접미사가 일치하는 최대 길이를 테이블로 저장
# 매칭 중 틀리면 테이블을 참고하여 비교 위치 건너뛰기 -> 불필요한 비교 생략

# 블로그를 통해 공부함, 혼자 풀지 않음
# 코드 이해도 -> 80%

def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    table = [0] * m
    j = 0

    # 1단계: 부분 일치 테이블 만들기
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    # 2단계: 본문 텍스트에서 패턴 찾기
    j = 0
    count = 0
    result = []

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]
        if text[i] == pattern[j]:
            if j == m - 1:
                count += 1
                result.append(i - m + 2)  # 위치는 1-based index
                j = table[j]
            else:
                j += 1

    print(count)
    print(*result)

T = input()
P = input()
kmp(T, P)

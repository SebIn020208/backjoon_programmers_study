# 1016번 제곱ㄴㄴ수 골드 1
# 4 9 16으로 나누어 떨어지지 않을 때 제곱 ㄴㄴ수
import sys
import math

input = sys.stdin.read
min_val, max_val = map(int, input().split())

size = max_val - min_val + 1
is_square_free = [True] * size

# 2부터 sqrt(max_val)까지의 수들에 대해
for i in range(2, int(math.sqrt(max_val)) + 1):
    square = i * i

    # min_val 이상에서 square의 배수 중 첫 번째 수 찾기
    start = ((min_val + square - 1) // square) * square

    for j in range(start, max_val + 1, square):
        is_square_free[j - min_val] = False

# 제곱ㄴㄴ수의 개수 출력
print(sum(is_square_free))


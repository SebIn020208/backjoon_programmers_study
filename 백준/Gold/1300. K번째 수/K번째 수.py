# 백준 1300번 골드1 K번째 수 이분탐색
def division(start, end, n, k):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in range(1, n + 1):
           total  += min(mid // i, n)
        if total >= k:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer

n = int(input())
k = int(input())
start = 1
end = k

result = division(start, end, n, k)
print(result)

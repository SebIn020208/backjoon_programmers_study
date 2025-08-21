def solution(k, tangerine):
    arr = sorted(tangerine)
    
    sum_arr = []
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            count += 1
        else:
            sum_arr.append(count)
            count = 1
    sum_arr.append(count)  # 마지막 그룹 추가
    
    sum_arr.sort(reverse=True)
    
    result = 0
    total = 0
    for num in sum_arr:
        total += num
        result += 1
        if total >= k:
            return result

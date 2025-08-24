from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for order in permutations(dungeons, len(dungeons)):  
        tired = k
        cnt = 0
        for min_req, cost in order:  
            if tired >= min_req:
                tired -= cost
                cnt += 1
            else:
                break
        answer = max(answer, cnt)
    
    return answer
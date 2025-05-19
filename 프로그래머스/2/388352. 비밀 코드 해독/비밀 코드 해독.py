from itertools import combinations

def solution(n, q, ans):
    answer = 0
    secretcode = list(combinations(range(1,n+1),5))
    
    for code in secretcode:
        condition = True
        for que in range(len(q)):
            if len(set(code) & set(q[que])) != ans[que]:
                condition = False
                break
                      
        if condition:
            answer += 1
    return answer
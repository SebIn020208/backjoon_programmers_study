#회원권 10일

#매일 한가지 제품 할인 
#하나씩만 구매 가능

#자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속 일치할 경우 회원권 구매

#회원권 구매하는 경우 리턴

# 키 값으로 Counter함수와 매칭

from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    # 원하는 제품 + 수량을 딕셔너리로
    want_dict = dict(zip(want, number))
    
    # 할인 품목 배열에서 10일씩 잘라보며 검사
    for i in range(len(discount) - 9):  # 마지막 시작점까지
        # 10일 연속 구간
        window = discount[i:i+10]       
        if Counter(window) == want_dict:
            answer += 1
            
    return answer

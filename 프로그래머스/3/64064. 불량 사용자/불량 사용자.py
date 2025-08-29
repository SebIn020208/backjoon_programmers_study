from itertools import permutations

def check(user, banned):  # user랑 banned가 일치하는지 확인
    if len(user) != len(banned):
        return False
    for i in range(len(user)):
        if banned[i] == "*":  # *이면 뭐든지 통과
            continue
        if user[i] != banned[i]:  # 다르면 실패
            return False
    return True

def solution(user_id, banned_id):
    result = []  # 경우의 수 저장

    # 순서 있는 뽑기
    for comb in permutations(user_id, len(banned_id)):
        ok = True
        for i in range(len(banned_id)):
            if not check(comb[i], banned_id[i]):
                ok = False
                break

        if ok:  # 모든 banned_id랑 맞았으면
            case = set(comb)   # 집합으로 바꿔서 (순서 제거)
            if case not in result:  # 중복 방지
                result.append(case)

    return len(result)

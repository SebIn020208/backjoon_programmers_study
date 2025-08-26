import math

def solution(fees, records):
    # fees = [기본 시간, 기본 요금, 단위 시간, 단위 요금]
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    in_dict = {}      # {차량번호: 입차시간} (아직 OUT 안된 차량 기록)
    total_time = {}   # {차량번호: 누적 주차시간}
    
    # 모든 입출차 기록 순회
    for record in records:
        in_time, car_num, state = record.split()
        h, m = map(int, in_time.split(":"))
        minute_time = h * 60 + m   # "HH:MM" → 분 단위로 변환
        
        if state == "IN":
            # 입차한 경우: 차량번호를 key로 입차 시간 저장
            in_dict[car_num] = minute_time
        else:  # state == "OUT"
            # 출차한 경우: 누적 주차 시간 갱신
            parked = minute_time - in_dict[car_num]
            total_time[car_num] = total_time.get(car_num, 0) + parked
            del in_dict[car_num]  # 입차 기록 제거
    
    # 아직 출차 안 한 차량은 23:59에 출차한 것으로 처리
    for car_num, in_time in in_dict.items():
        parked = (23 * 60 + 59) - in_time
        total_time[car_num] = total_time.get(car_num, 0) + parked
    
    # 차량별 요금 계산
    answer = []
    for car_num in sorted(total_time.keys()):  # 차량번호 오름차순 정렬
        time = total_time[car_num]
        
        if time <= basic_time:
            # 기본 시간 이하라면 기본 요금만 부과
            fee = basic_fee
        else:
            # (총 시간 - 기본 시간)을 단위 시간으로 나누고 올림 → 단위 요금 곱하기
            fee = basic_fee + math.ceil((time - basic_time) / unit_time) * unit_fee
        answer.append(fee)
    
    return answer

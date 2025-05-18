def solution(schedules, timelogs, startday):
    answer = 0
    # 직원별 희망 출근 시간 + 10분
    schedules = [convert(s) + 10 for s in schedules]

    for i in range(len(timelogs)): 
        person = timelogs[i]
        schedule = schedules[i]
        working_days = 0
        cur_day = startday - 1

        for time in person:
            cur_day += 1
            weekday = cur_day % 7

            if weekday == 0 or weekday == 6:
                continue
            if convert(time) > schedule:
                break
            working_days += 1

        if working_days == 5:
            answer += 1

    return answer

def convert(time):
    time = str(time).zfill(4)
    h, m = int(time[:-2]), int(time[-2:])
    return h * 60 + m

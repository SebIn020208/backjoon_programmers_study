def solution(plans):
    result = []
    tasks = []

    for name, start, duration in plans:
        h, m = map(int, start.split(":"))
        start_time = h * 60 + m
        tasks.append([start_time, name, int(duration)])
    
    tasks.sort()
    
    stack = []
    
    for i in range(len(tasks) - 1):
        cur_start, cur_name, cur_dur = tasks[i]
        next_start = tasks[i+1][0]
        time_gap = next_start - cur_start
        
        if cur_dur <= time_gap:
            result.append(cur_name)
            remain = time_gap - cur_dur
            
            while remain > 0 and stack:
                last_name, last_dur = stack.pop()
                if last_dur <= remain:
                    remain -= last_dur
                    result.append(last_name)
                else:
                    stack.append((last_name, last_dur - remain))
                    remain = 0
        else:
            stack.append((cur_name, cur_dur - time_gap))
    
    result.append(tasks[-1][1])
    
    while stack:
        result.append(stack.pop()[0])
    
    return result

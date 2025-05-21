def solution(numbers, target):
    array = [0]
    answer = 0
    for num in numbers:
        temp = []
        for s in array:
            temp.append(s + num)
            temp.append(s - num)
        array = temp
        
    for s in array:
        if s == target:
            answer += 1
            
    return answer
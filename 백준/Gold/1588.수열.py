#시간초과 문제 해결 필요

rules = {
    0: [0],
    1: [1, 3, 2],
    2: [2, 1, 1],
    3: [2, 3, 2],
}

n = int(input())
left, right = int(input()), int(input())
second = int(input())

length_cache = {}

def get_length(num, sec):
    if sec == 0:
        return 1
    if (num, sec) in length_cache:
        return length_cache[(num, sec)]
    if num == 0:
        length_cache[(num, sec)] = 1
    else:
        total = 0
        for next_num in rules[num]:
            total += get_length(next_num, sec - 1)
        length_cache[(num, sec)] = total
    return length_cache[(num, sec)]

def count_digits(num, sec, left, right):
    if sec == 0:
        if left <= 0 < right and num in [1, 2, 3]:
            result = [0, 0, 0]
            result[num - 1] += 1
            return result
        return [0, 0, 0]

    result = [0, 0, 0]
    offset = 0

    for next_num in rules[num]:
        curr_len = get_length(next_num, sec - 1)
        if offset >= right:
            break
        seg_l = max(0, left - offset)
        seg_r = max(0, right - offset)

        if seg_l < seg_r:
            temp = count_digits(next_num, sec - 1, seg_l, seg_r)
            for i in range(3):
                result[i] += temp[i]

        offset += curr_len

    return result

count_array = count_digits(n, second, left, right+1)
print(count_array)

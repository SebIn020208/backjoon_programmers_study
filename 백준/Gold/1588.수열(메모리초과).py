# 시간 초과 전에 풀이 한 코드

n = int(input())
left, right = int(input()), int(input())
second = int(input())

rules = {
    0: [0],
    1: [1, 3, 2],
    2: [2, 1, 1],
    3: [2, 3, 2],
}

sequence = rules[n]

for _ in range(1, second):
    new_sequence = []
    for num in sequence:
        new_sequence.extend(rules[num])
        if len(new_sequence) > right:
          break
    sequence = new_sequence

part_sequence = sequence[left:right+1]

count_array = [0, 0, 0]
for num in part_sequence:
    if num == 1:
        count_array[0] += 1
    elif num == 2:
        count_array[1] += 1
    elif num == 3:
        count_array[2] += 1

print(count_array)

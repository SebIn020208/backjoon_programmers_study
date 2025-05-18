def solution(storage, requests):
    answer = 0
    
    # 테두리를 "0"으로 채워서 외부와 연결되도록 처리
    storage = [list("0" + row + "0") for row in storage]
    width = len(storage[0])
    storage.insert(0, list("0" * width))
    storage.append(list("0" * width))

    # 요청 처리
    for req in requests:
        if len(req) == 1:
            fork(storage, req)
        else:
            crane(storage, req[0])

    # 아직 남아있는 알파벳 박스 세기
    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] not in ["0", "1"]:
                answer += 1

    return answer


def fork(storage, box):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    targets = []

    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] == box:
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if storage[ni][nj] == "0":
                        targets.append((i, j))
                        break

    for i, j in targets:
        storage[i][j] = "0"
        is_outside(storage, i, j)


def crane(storage, box):
    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] == box:
                storage[i][j] = "1"
                is_outside(storage, i, j)


def is_outside(storage, x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    connected = False

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if storage[nx][ny] == "0":
            storage[x][y] = "0"
            connected = True
            break

    if connected:
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if storage[nx][ny] == "1":
                storage[nx][ny] = "0"
                is_outside(storage, nx, ny)

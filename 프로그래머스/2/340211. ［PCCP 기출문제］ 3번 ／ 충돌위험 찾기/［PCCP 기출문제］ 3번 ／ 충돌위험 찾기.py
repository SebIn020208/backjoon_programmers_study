from collections import Counter

def solution(points, routes):
    def bfs(route):
        idx = 0
        path = []
        for i in range(len(route) - 1):
            start_x, start_y = points[route[i] - 1]
            end_x, end_y = points[route[i + 1] - 1]
            
            while start_x != end_x:
                path.append((start_x, start_y, idx))
                if start_x < end_x:
                    start_x += 1
                else:
                    start_x -= 1
                idx += 1

            while start_y != end_y:
                path.append((start_x, start_y, idx))
                if start_y < end_y:
                    start_y += 1
                else:
                    start_y -= 1
                idx += 1
        path.append((start_x, start_y, idx))
        return path

    spots = [point for point in points]
    all_positions = []

    for route in routes:
        all_positions.extend(bfs(route))
    count_positions = Counter(all_positions)
    result = 0
    for cnt in count_positions.values():
        if cnt >= 2:
            result += 1

    return result

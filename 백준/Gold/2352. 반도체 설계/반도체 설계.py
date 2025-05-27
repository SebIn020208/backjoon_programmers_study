# 백준 2352번 골드2 반도체 설계
from bisect import bisect_left 

n = int(input())
port = list(map(int, input().split()))
line = [port[0]]

for node in range(1, n):
  if port[node] > line[-1]:
    line.append(port[node])
  else:
    idx = bisect_left(line, port[node])
    line[idx] = port[node]

print(len(line))
  

    
    


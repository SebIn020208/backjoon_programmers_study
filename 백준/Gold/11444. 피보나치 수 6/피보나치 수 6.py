# 백준 11444번 피보나치 수6 골드2 분할정복
def Fibo(num):
  if num <= 2:
    return F[num]
  elif F[num] > 0:
    return F[num]
  else:
    half = num // 2
    if num % 2 == 0:
      f0 = Fibo(half)
      f1 = Fibo(half-1)
      F[num] = ((2*f1 + f0)*f0)%1000000007
      return F[num]
    else:
      f0 = Fibo(half+1)
      f1 = Fibo(half)
      F[num] = (f0**2 + f1**2)%1000000007
      return F[num]

from collections import defaultdict
n = int(input())
F = defaultdict(int)
F[1], F[2] = 1,1

print(Fibo(n))
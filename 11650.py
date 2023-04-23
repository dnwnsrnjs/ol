n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))
lst.sort()
for a, b in lst:
    print(a, b)
n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((b, a))
lst.sort()
for a, b in lst:
    print(b, a)


# n = int(input())
# lst = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     lst.append((x, y))
# lst.sort(key = lambda x:(x[1], x[0]))
# for x, y in lst:
# print(x, y)
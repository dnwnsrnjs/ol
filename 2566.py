lst = []
for i in range(9):
    t = list(map(int, input().split()))
    lst.append(t)
m = 0
행 = 0
열 = 0
for i in range(9):
    for j in range(9):
        if m < lst[i][j]:
            m = lst[i][j]
            행 = i
            열 = j

print(m)
print(행 + 1, 열 + 1)
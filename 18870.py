n = input()
lst = list(map(int, input().split()))
ol = lst.copy()
lst = set(lst)
lst = sorted(lst)
d = {}
for i, v in enumerate(lst):
    d[v] = i 
for i in ol:
    print(d[i], end = " ")
s = set()
n = int(input())
for i in range(n):
    s.add(input())

lst = list(s)
lst.sort(key = lambda x: (len(x), x) )
print(*lst, sep = "\n") 
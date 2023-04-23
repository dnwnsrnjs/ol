lst = [0] * 31
for _ in range(28):
    n = int(input())
    lst[n] = 1

for i in range(1, 31):
    if lst[i] == 0:
        print(i)
## 위의 코드는 리스트에 0을 31개 넣어서 입력받은 수를 0에서 1로 전환하여 0이 그대로 남아있다면 그 인덱스는 출석 안한 번호이다. -> 답이다


# l = list(range(1, 31))
# for _ in range(28):
#     n = int(input())  
#     lst.remove(n)
# print(min(lst))
# print(max(lst))


# s = set(range(1, 31))
# for _ in range(28):
#     idx = int(input())
#     s.remove(idx)
# print(*s, sep="\n")
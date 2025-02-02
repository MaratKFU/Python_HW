lst = list(map(int, input().split()))
x = int(input())
nums = []
for i in range(len(lst)):
    if lst[i] == x:
        nums.append(i)
print(*nums)

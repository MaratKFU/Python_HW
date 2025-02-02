count = -1
summ = 0
n = 1
while n != 0:
    n = int(input())
    summ += n
    count += 1
print(summ / max(count, 1))

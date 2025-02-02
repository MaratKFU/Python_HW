count = 0
summ = 0
n = 1
while True:
    n = int(input())
    if n > 100:
        break
    if n < 10:
        continue
    summ += n
    count += 1
print(summ / max(count, 1))

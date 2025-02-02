print("¬ведите список слов:")
mas = input().split()
countNums = {}
for i in range(len(mas)):
    if mas[i] in countNums.keys():
        countNums[mas[i]] += 1
    else:
        countNums.update({mas[i]: 1})
print(*countNums.values())

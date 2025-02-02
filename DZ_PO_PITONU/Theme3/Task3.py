mas = list(map(int, input().split()))
srArifm = sum(mas)/len(mas)
mas2 = list()
for i in mas:
    if i >= srArifm:
        mas2.append(i)
print(f"Среднее арифметическое равно {int(srArifm)}")
print(f"Всего значений больше среднего арифметического: {len(mas2)}")
print(f"Список значений: {", ".join(mas2)}")

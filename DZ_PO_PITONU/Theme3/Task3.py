mas = list(map(int, input().split()))
srArifm = sum(mas)/len(mas)
mas2 = list()
for i in mas:
    if i >= srArifm:
        mas2.append(i)
print(f"������� �������������� ����� {int(srArifm)}")
print(f"����� �������� ������ �������� ���������������: {len(mas2)}")
print(f"������ ��������: {", ".join(mas2)}")

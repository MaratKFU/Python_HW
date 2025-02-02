s = input()
if ", " in s:
    s = list(map(int, s.split(", ")))
else:
    s = list(map(int, s.split()))
print(len(set(s)))

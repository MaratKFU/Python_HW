def modify_list(l):
    i = 0
    while True:
        if i == len(l):
            break
        if l[i] % 2:
            l.pop(i)
        else:
            l[i] //= 2
            i += 1

#Пример
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)

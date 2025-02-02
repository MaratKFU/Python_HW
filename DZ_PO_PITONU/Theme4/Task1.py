def containsSpecificSymbol(s):
    for i in s:
        if ord(i) in range(33, 39):
            return True
    return False


def containsNum(s):
    for i in s:
        if i.isdigit():
            return True
    return False


while(True):
    email = input("Пожалуйста, введите адрес электронной почты: ")
    if (email.endswith("@kpfu.ru")== 0):
        print("Требуется указать адрес в доменной зоне kpfu.ru")
    else:
        break
while(True):
    password = input("Пожалуйста, введите новый пароль: ")
    condition1 = containsNum(password)
    condition2 = ((not password.islower()) and (not password.isnumeric()))
    condition3 = len(password) > 7
    condition4 = containsSpecificSymbol(password)
    conditions = condition1 and condition2 and condition3 and condition4
    if(conditions):
        tries = 4
        while (tries):
            password2 = input("Пожалуйста, повторите пароль: ")
            if (password == password2):
                print("Вы успешно прошли регистрацию")
                break
            else:
                tries -= 1
                print(f"Пароли не совпадают, количество оставшихся попыток: {tries}")
        if tries > 0:
            break
    else:
        print("Пароль не соответствует следующим требованиям:")
        if not(condition1):
            print("В нём нет хотя бы одной цифры")
        if not(condition2):
            print("В нём нет хотя бы одной заглавной буквы")
        if not(condition3):
            print("Он короче 8 символов")
        if not(condition4):
            print("Он не содержит хотя бы одного специального символа (!, \", #, $, %, &)")

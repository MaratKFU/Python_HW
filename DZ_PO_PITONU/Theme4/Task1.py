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
    email = input("����������, ������� ����� ����������� �����: ")
    if (email.endswith("@kpfu.ru")== 0):
        print("��������� ������� ����� � �������� ���� kpfu.ru")
    else:
        break
while(True):
    password = input("����������, ������� ����� ������: ")
    condition1 = containsNum(password)
    condition2 = ((not password.islower()) and (not password.isnumeric()))
    condition3 = len(password) > 7
    condition4 = containsSpecificSymbol(password)
    conditions = condition1 and condition2 and condition3 and condition4
    if(conditions):
        tries = 4
        while (tries):
            password2 = input("����������, ��������� ������: ")
            if (password == password2):
                print("�� ������� ������ �����������")
                break
            else:
                tries -= 1
                print(f"������ �� ���������, ���������� ���������� �������: {tries}")
        if tries > 0:
            break
    else:
        print("������ �� ������������� ��������� �����������:")
        if not(condition1):
            print("� �� ��� ���� �� ����� �����")
        if not(condition2):
            print("� �� ��� ���� �� ����� ��������� �����")
        if not(condition3):
            print("�� ������ 8 ��������")
        if not(condition4):
            print("�� �� �������� ���� �� ������ ������������ ������� (!, \", #, $, %, &)")

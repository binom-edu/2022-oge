# определить, какое из введенных чисел больше
# вложенное ветвление

a, b = map(int, input().split())

if a > b:
    print('Первое больше')
else:
    if a == b:
        print('Равны')
    else:
        print('Второе больше')
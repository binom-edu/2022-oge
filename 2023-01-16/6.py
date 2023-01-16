# дано число. проверить, является ли оно двузначным

a = int(input())

if a > 9 and a < 100:
    print('yes')
else:
    print('no')

if 9 < a < 100:
    print('yes')
else:
    print('no')
# дано число. проверить, что оно не заканчивается на 3 или 6

a = int(input())
if not (a % 10 == 3 or a % 10 == 6):
    print('yes')
else:
    print('no')
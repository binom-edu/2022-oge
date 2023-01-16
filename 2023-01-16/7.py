# дано число. проверить, что оно заканчивается на 3 или на 6

a = int(input())
if a % 10 == 3 or a % 10 == 6:
    print('yes')
else:
    print('no')
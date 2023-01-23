# дано число. посчитать сумму его цифр
n = int(input())
ans = 0
n_copy = n
while n > 0:
    ans += n % 10
    n //= 10
print(f'Сумма цифр числа {n_copy} равна {ans}')
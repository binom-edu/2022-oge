# дано число. определить его максимальную цифру
n = int(input())
ans = 0
while n > 0:
    d = n % 10 # последняя цифра
    if d > ans:
        ans = d
    n //= 10
print(ans)
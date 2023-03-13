def isPrime(n):
    for d in range(2, n):
        if n % d == 0:
            return False
        if d ** 2 >= n:
            break
    return True

x = int(input())
if isPrime(x):
    print('yes')
else:
    print('no')
# найти максимум из двух чисел
# неполная форма
a, b = map(int, input().split())
m = a
if b > m:
    m = b
print(m)
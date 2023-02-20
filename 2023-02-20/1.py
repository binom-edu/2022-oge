s = 'abacaba'
# посчитать, сколько раз встречается буква a
ans = 0
for i in s:
    if i == 'a':
        ans += 1
print(ans)
print(s.count('a'))
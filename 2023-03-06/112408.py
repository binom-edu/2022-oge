s = input()
n = len(s)
ans = 0
i = 0
j = n - 1
while i < j:
    while i < n and s[i] == 'B':
        i += 1
    while j >= 0 and s[j] == 'R':
        j -= 1
    if i < j:
        ans += 2
        i += 1
        j -= 1
cb = s.count('B') - ans // 2
cr = s.count('R') - ans // 2
print('B' * cb + 'R' * cr)
print(ans)
# заменить в строке все символы а на символ х
s = input()
ans = ''
for i in s:
    if i == 'a':
        ans += 'x'
    else:
        ans += i

print(ans)
s = s.replace('a', 'x')
print(s)
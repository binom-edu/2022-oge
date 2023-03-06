s = input()
pos = s.find('R')
if pos == -1:
    print(s)
    exit(0)
s1 = s[:pos]
s2 = s[pos:]
cnt = s2.count('B')
print(s1 + s2.replace('B', ''))
print(cnt)
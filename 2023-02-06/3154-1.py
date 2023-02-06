# a = [int(i) for i in input().split()]
# ans = 0
# for i in a:
#     if i > 0:
#         ans += 1
# print(ans)

print(len([int(i) for i in input().split() if int(i) > 0]))
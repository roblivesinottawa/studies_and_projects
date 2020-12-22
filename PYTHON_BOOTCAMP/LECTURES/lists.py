# data = [20, 34, 56, 86, 90, 190, 65]
# data[0] = 100
# print(max(data))

# total = 0
# for y in data:
#     total += y
#     print(total, end=' ')


positive_integers = [2,3,4,5,6,7,8,9]

findmax = 0
for num in positive_integers:
    if num > findmax:
        findmax = num
print(findmax)

# print(max(positive_integers))
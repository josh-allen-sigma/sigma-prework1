list = [7, -3, 3, 4, 5, 110]
maxnum = list[0]
minnum = list[0]
for num in list:
    if num > maxnum:
        maxnum = num
    elif num < minnum:
        minnum = num
    else:
        continue

print([minnum, maxnum])

l1 = [2, 6, 8, 9, 3, 9, 3, 6, 8, 5]
l1 = sorted(l1)
l2 = []
for i in range(len(l1)):
    if l1[i] == l1[i + 1]:
        l2.append(l1[i])
print(l2)
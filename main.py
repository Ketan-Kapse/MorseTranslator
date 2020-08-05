import itertools

a = list()
item = 1
b = list()
n = 4
while item != 0:
    item = input("enter")
    if item == "q":
        break
    elif len(item) > 4:
        new_item = [(item[i:i + n]) for i in range(0, len(item), n)]
        for j in range(len(new_item)):
            a.append(new_item[j])

    else:
        a.append(item)
for i in range(len(a)):
    if a[i] == "....":
        b.append("a")
    elif a[i] == ".":
        b.append("e")

print(b)

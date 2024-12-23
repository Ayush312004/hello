def intersection(l1, l2):
    res = []

    for student in l1:
        if student in l2:
            res.append(student)

    return res


def union(l1, l2):
    res = l2.copy()

    for student in l1:
        if not student in l2:
            res.append(student)

    return res


def diff(l1, l2):
    res = []

    for student in l1:
        if not student in l2:
            res.append(student)

    return res


a = [1, 2, 3, 4, 5, 6, 7]
b = [2, 3, 6, 7, 9, 10]
c = [2, 4, 6, 8, 10, 12]


print(__doc__)

print(f"A = {a}\nB = {b}\nC = {c}\n")

print("a.", end=" ")
print(intersection(a, b))
print("b.", end=" ")
print(diff(union(a, b), intersection(a, b)))
print("c.", end=" ")
print(diff(diff(c, b), a))
print("d.", end=" ")
print(diff(union(a, c), b))

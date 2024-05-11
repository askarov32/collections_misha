# set изменяемая, но он не хранит дубликаты
# set нет индексации, неотсортированный

set1 = {1, 2, 4, 4}
print(set1)

set2 = {"misha", "insar", 2}

for i in set1:
    print(i)

print(5 in set1)

set1.add(8)
set1.add(10)
print(set1)

set1.update([1, 2, 3, 3, 3, 3, 3])
print(set1)

set1.remove(3)
set1.discard(1)
print(set1)

# set1.clear()
# print(set1)

# del set1
# print(set1)

print(len(set1))

set3 = set1.union(set2)
print(set3)

set4 = set(("mskja", "feferf", "dwedef"))
print(set4)


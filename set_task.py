set1 = {1, 2, 3, "a"}
set2 = {3, 2, 5, "a", "b"}
set4 = {9}

set3 = set1.intersection(set2)
print(set3)
print(set1.isdisjoint(set4))
set5 = set1.difference(set2)
print(set5)
print(set2.difference(set1))

students = {"misha", "insar"}
otlichniki = {"misha"}

print(otlichniki.issubset(students))

mats = ["blyat", "suka", "eblan", "huy"]

set6 = set()
while True:
    x = input()
    if x == "stop":
        break
    set6.add(x)

    for i in mats:
        if i in x:
            set6.remove(x)

print(set6)


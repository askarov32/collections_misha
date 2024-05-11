list1 = [1, 2, 3]

# list остортируемый, индексация присутсвует, изменяемый

tuple1 = ("apple", "banana", "cherry", "melon", "sobaka")

# tuple отсортируемый, индексация присутсвует, неменяемый

string = "misho"
string = string.replace("o", "a")
print(string)

tuple_list = list(tuple1)

tuple_list[0] = "kiwi"
tuple1 = tuple(tuple_list)
print(tuple1)

# написать тюпл с овощами, потом вывести через цикл все, потом заменить один овощ на sobaka, заменить все буквы а на b во всех элементах

i = 0
while i < len(tuple1):
    print(tuple1[i])
    i += 1

print("")

list2 = []
for i in tuple1:
    i = i.replace("a", "b")
    list2.append(i)
tuple1 = tuple(list2)
print(tuple1)

list3 = ["misha"]

tuple2 = tuple(list2)
print(tuple2)

tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = ("mashina",)
print(type(tuple4))

tuple5 = (1, 2, 3, 3, 3, 8, 8)
print("в этом тюпле", tuple5.count(8))

print(tuple5.index(8))

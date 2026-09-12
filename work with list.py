lst = ['Apple','Guava','Mango','Banana','Kiwi']
print("length of list:",len(lst))
print("First Element:",lst[0])
print("First Element;", lst[-1])
lst.append('Papaya')
print("Update List:", lst)

lst.append('Guava')
print("Update List:", lst)

lst.sort()
print("Sorted list:", lst)

lst.pop(1)
print("Update List:", lst)

lst.reverse()
print("Reversed List:", lst)

print("Multiplication on List:", lst*2)
lst = lst[:4]
print("Sliced:List", lst)

lst.clear()
print("Updated List:", lst)
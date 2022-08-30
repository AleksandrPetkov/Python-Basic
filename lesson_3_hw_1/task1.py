list1 = ["a", "3.5"]
print("List1 before add 'c':",  list1)
list1.insert(1, 'c')
print("List1 after add 'c':", list1)
list1.remove("c")
print("List1 before replace 'a' and '3.5'", list1)
list1.reverse()
print("List1 after replace 'a' and '3.5'", list1)
list2 = [5, 9]
print("List2 before math changes:", list2)
for i in range(len(list2)):
    list2[i] += 3
    print("List2 after math changes:", list2)

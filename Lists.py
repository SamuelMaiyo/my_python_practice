mylist = ["banana", "cherry","apple"]
print(mylist)

item = mylist[-1]
print(item)

for i in mylist:
    print(i)

if "mango" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist))

mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item = mylist.remove("banana")
print(mylist)

item = mylist.clear()
print(mylist)

list1 = [1, 2, 3, 4, -4, -7]

object = list1.sort()
print(list1)

new_list = sorted(list1)
print(list1)

list_org = ["tea", "coffee", "milk"]

list_cpy = list_org.copy()
list_cpy = list(list_org)
list_cpy = list_org[:]
print(list_cpy)

list_cpy.append ("lemon")
print(list_cpy)
print(list_org)

# List Comprehension
list2 = [1, 2, 3, 4, 5, 6]

b = [i*i for i in list2]
print(list2)
print(b)
mytuple = ("Max", 23, "Ohio", 'a', 'a', '4')
print(type(mytuple))

tuple1 = "Max",
print(type(tuple1))

tuplex = ("max")
print(type(tuplex))

item = mytuple[2]
print(item)

# mytuple[1] = "Tim" #Tuples are immutable

for i in mytuple:
    print(i)

if "Mix" in mytuple:
    print("yes")
else:
    print("no")

print(len(mytuple))

print(mytuple.count("a"))

print(mytuple.index("a"))

#convert from tuple to list and vice versa

my_list = list(mytuple)
print(my_list)

tuple_x = tuple(my_list)
print(tuple_x)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:6]
print(b)

#step function
b = a[1::2]
print(b)

#negative step function
b = a[::-1]
print(b)

# unpecking
the_tuple = ("Max", 23, "Ohio",)
name, age, city = the_tuple
print(name)
print(age)
print(city)

thy_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
i1, *i2, i3 = thy_tuple
print(i1)
print(i2)
print(i3)

# Comparing a list and a tuple

import sys
import timeit
A_list =[0, 1, 2, "Hello", True]
A_tuple =(0, 1, 2, "Hello", True)
print(sys.getsizeof(A_list), "bytes")
print(sys.getsizeof(A_tuple), "bytes")

print(timeit.timeit(stmt = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", number = 1000000))
print(timeit.timeit(stmt = "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)", number = 1000000))
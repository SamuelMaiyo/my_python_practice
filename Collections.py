# Collections - counter, namedtuple, orderdict, default dict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict

# Counter
a = "aaaabbcccddeeee"
my_counter   = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common())
print(my_counter.most_common(2))
print(my_counter.most_common(2)[0][0])

print(list(my_counter.elements()))

#Namedtuple

Point = namedtuple("Point", "x,y")
pt = Point(1, -2)

print(pt)
print(pt.x, pt.y)

#OrderedDict - Print dictionary in order of which it was inserted
orderd_dict = OrderedDict()
orderd_dict['b'] = 2
orderd_dict['c'] = 3
orderd_dict['d'] = 4
orderd_dict['a'] = 1

print(orderd_dict)
# Sets: Unordered, Mutable, no duplicates
myset = {1, 2, 3}
print(myset)

# No Duplicates
myset = {1, 2, 3, 1, 3}
print(myset)

myset_1 = set([3, "Hi", True])
print(myset_1)
myset_1 = set("Hello")
print(myset_1)

myset_1 = set()
print(type(myset_1))

# Mutable
myset_2 = set()
myset_2.add(1)
myset_2.add(2)
myset_2.add(3)
myset_2.add(4)

print(myset_2)

myset_2.remove(3) # Cannot remove a non-existent element 
print(myset_2)

myset_2.discard(6) # Removes a non-existent element 
print(myset_2)

myset_2.clear() # Empty set 
print(myset_2)

print(myset.pop()) # removes an arbitraty value of the set

## Iterate
myset_3 = set()
myset_3.add(10)
myset_3.add(20)
myset_3.add(30)
myset_3.add(40)

for i in myset_3:
    print(i)

if 20 in myset_3:
    print("yes")

# Union and intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens) # Uniion combines elements form 2 sets without duplication
print(u)

i = odds.intersection(evens) # Intersection returns same elements in 2 sets
print(i)    

i = odds.intersection(primes) # Intersection returns same elements in 2 sets
print(i) 

# Difference in sets
SetA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
SetB = {0, 2, 4, 6, 8}

diff = SetA.difference(SetB)
print(diff)

diff = SetB.difference(SetA)
print(diff)

diff = SetA.symmetric_difference(SetB)
print(diff)

SetA.update(SetB) # Update one set with the other
print(SetA)

SetA.intersection_update(SetB) # Update one set with the intersectionof the other
print(SetA)

SetA.difference_update(SetB) # Remove all elements of another set from this set
print(SetA)

SetA.symmetric_difference_update(SetB) # Remove all elements of another set from this set
print(SetA)

# Supersets and Subsets
Set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
Set2 = {1, 2, 3, 4, 5}
Set3 = {10, 20}
print(Set1.issubset(Set2))
print(Set2.issubset(Set1))

print(Set1.issuperset(Set2))
print(Set2.issuperset(Set1))

print(Set1.isdisjoint(Set2))
print(Set2.isdisjoint(Set1))
print(Set2.isdisjoint(Set3))

# Copy set
SetB = SetA.copy()
SetB.add(7)
print(SetB)
print(SetA)
 
SetA = SetB
print(SetB)
SetB.add(7)
print(SetB)
print(SetA)

SetB = SetA.copy()

# Frozen set
X = frozenset([1, 2, 3, 4, 5])
print(X)

X.add(8)
print(X) # Results to error. Set is immutable
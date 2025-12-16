a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print(a-b)      # difference
print(a|b)      # union
print(a&b)      # intersection
print(a^b)      # symmetric difference
print(a.isdisjoint(b))
print(a.issubset(b))
print(a.issuperset(b))

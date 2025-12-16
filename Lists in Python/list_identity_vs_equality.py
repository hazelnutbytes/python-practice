a = [1,2,3]
b = [1,2,3]
print(a is b)  # False
print(a == b)  # True

b = a
b.append(4)
print(a)       # [1,2,3,4]
print(a is b)  # True

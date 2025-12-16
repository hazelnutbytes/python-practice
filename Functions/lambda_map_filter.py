# Lambda
square = lambda x: x*x
print(square(5))

nums = [1,2,3,4,5]
doubled = list(map(lambda x: x*2, nums))
print(doubled)

even_nums = list(filter(lambda x: x%2==0, nums))
print(even_nums)

# is type data like list but unchanged

# syntax
my_tuple1 = (1, 2, 3)
my_tuple2 =("tiep", "thang", "huy")

# print tuple
print(my_tuple1)
print(my_tuple2)

# how to change value in tuple
x  = (1, 2, 3)
y = list(x)
y[1] = 4
x = tuple(y)
print(x)

# can't add member in tuple so change datatype to list then convert to tuple
# add 2 tuple use + 
# method in tuple 
    # count
    # index
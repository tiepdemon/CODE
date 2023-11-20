# define a set
my_set1 = {4, 5, 3}
z = my_set1.pop()   
print(z)
print(my_set1)
my_set2 = {"hello", "world"}

# method in set
    # add(x) : add value x to end set
    # remove (x) : remove value x in set (err if x not in set, so use discard or intersection_update())
    # discard (x) : remove value x in set if x not ịn set will not error
    # len(x) : return number of set x
    # sorted(x, y,reverse = z) : sort set x and return a list with key y, bool z
    # kiểu set chỉ giữ lại các phần tử không trùng lặp vậy nên muốn thêm phần tử vào set
# sẽ cần dùng update(x) để thêm set x vào
    # x.update(y) : add set y to set x
    # x = x.union(y) : add set y to set x
    # x.intersection_update(y) : will keep only the items in both sets
    # z = x.intersection(y) : return a set with items in both set
    # x.difference(y) : return a set belong x but not belong y
    # x.symmetric_difference(y) : return a set belong x or belong y ( 1 and True is same)
    # x.symmetric_difference_update(y) : update x with belong x or belong y
    # x.union(y) : return a set has both x and y
    # x.update(y) : update x has both x and y

list_num = list((1,2,3))
list_str = ["dao", "le", "man"]
# # in danh sach
# print(list_num)
# print(list_str)
# #in phan tu
# print(list_str[1])
# for item in list_num : print(item)
# #check item
# if "dao" in list_str :
#     print("có dao trong tap")
# # nối thêm vào cuối
# list_str.append("man")
# # thêm vào vị trí bất kì
# list_str.insert(1,"mai")
# # nối 2 chuỗi
# list_str.extend(list_num)
# print(list_str)
# #xoá phần tử
#     # theo tên
# list_str.remove(list_str[1])
# list_str.remove("dao")
# del list_str[0]
# print(list_str)
#     #theo thứ tự
# list_str.pop(0)
#     # xoá toàn bộ
# list_str.clear()

# #loop
# for x in list_num :
#     print(x)
#     x += 1
#     print(x)

new_list = [x for x in list_str if x != "dao"]
print(new_list)
for x in list_str : 
    if x == "man" : print(x)

#sort
num1 = [1, 3, 2, 5, 4]
num1.sort(reverse=True)
print(num1)
    #thuộc tính của sort có thể là 
    #key
    #reverse
#nếu muốn tham trị dùng hàm num2 = num1.copy() hoặc dùng num2 = list(num1) còn tham chiếu thì dùng =
num2 = num1.copy()

#các cách thêm vào một chuỗi
    # thêm từng phần tử
num1.append(1) # thêm vào cuối phần tử 1
num1 + num2 # thêm list 2 vào list 1
num1.extend(num2) #thêm list2 vào list 1

#method in list
    #copy() : sao chép mảng theo kiểu tham trị
    #clear() : xoá mảng
    #append(x) : add value x in to end list
    #count(x, y, z) : return count x with position x  to position y 
    #extend() : add element to the end list
    #index() : return the index first element with the specified value
    #insert(x , y) : add value y into position x
    #pop(x) : remove value in position x
    #remove(x) : remove value with value x
    #sort(value, reverse = x) : sort with value, x = true or false default rervese = false
    #reverse() : reverse list

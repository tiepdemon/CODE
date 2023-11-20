str1 = "hello" #str
i = 1 #int
f = 1.5 #float
c1 = complex(1,2) #complex
c2 = 1 + 2j #complex

#Sequence Types
l = [1, 2, 3] #list : can change
    # methods
l.append(4) # thêm vào cuối
l.insert(1, 2) # thêm 2 vào vị trí 1
l.extend([5,6]) # nối list, (Bất cứ loại nào cx đc)
l.remove(1) # xoá theo đối tượng
l.pop(2) # xoá theo chỉ mục - xoá 3, () là xoá vị trí cuối cùng
del l[0] # xoá vị trí thứ 0
l.clear() # xoá toàn bộ
t = ("h", "y") #type : can't change
r = (1, 6, 2) #range : (start, end, step)
d = dict(name = "huy", age = 18) #dict : truy nhập bằng key và value
s = {"apple", "banana", "cherry"} #set : can change, ko stt
fs = frozenset({"apple", "banana", "cherry"}) #frozenset : can't change, ko stt
b = True #bool : true/ false

#kiểu byte : chủ yếu thao tác với các dãy nhị phân : hình ảnh âm thanh
# không làm thay đổi dữ liệu gốc

# Kiểu dữ liệu bytes (bất biến)
my_bytes = b'\x01\x02\x03'
# Không thể thay đổi my_bytes
# my_bytes[0] = 0x04  # Gây lỗi

# Kiểu dữ liệu bytearray (khả năng thay đổi)
my_bytearray = bytearray(b'\x01\x02\x03')
# Có thể thay đổi my_bytearray
my_bytearray[0] = 0x04  # Hợp lệ

# Kiểu dữ liệu memoryview (cho phép xem dữ liệu)
my_bytes = b'\x01\x02\x03'
view = memoryview(my_bytes)
# Bạn có thể sử dụng view để xem dữ liệu trong my_bytes

# bytes khi bạn cần một kiểu dữ liệu bất biến, 
# bytearray khi bạn cần một kiểu dữ liệu có khả năng thay đổi,
# memoryview khi bạn cần xem dữ liệu mà không cần sao chép.

#Ép kiểu
ek1 = float(1) # ek1 = 1.0
ek2 = str(1) # ek2 = "1"

#dùng """ để in nguyên văn cả cách
str2 = """Hello
i'm tiep"""
print(str2)




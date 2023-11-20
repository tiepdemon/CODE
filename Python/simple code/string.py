# Khai báo chuỗi 
str1 = "hello world"
str2 = "I'm Tiep"

print(str1[0])#Lấy 1 ký tự
print(len(str1)) #độ dài chuỗi
print("he" in str1) #kiểm tra sự tồn tại
my_string = "  Hello,      World!  "
trimmed_string = my_string.strip()  # Loại bỏ khoảng trắng đầu hoặc cuối câu
# Loại bỏ khoảng trắng
print(trimmed_string)
words = my_string.split() #tách chuỗi
clean_string = " ".join(words)
print(clean_string)

# cắt chuỗi
str3 = "hello world"
print(str3[:4]) #in từ 0-3 : hell
print(str3[2:4]) #in từ 2-3 : ll
print(str3[6:]) #in từ 0-3 : world

#Nối chuỗi
str3 = str1 + str2

#in hoa in thường
print(str1.upper())
print(str1.lower())

#find and replace
print(str1.find("o")) #tìm vị trí đầu tiên
print(str1.rfind("o")) #tìm vị trí cuối cùng
# muón tìm vị trí thứ i ta sẽ thông qua đệ qui tìm i-1 -> 0 
print(str1.replace("H", "T")) # thay thế tất cả H bằng T
print(str1.replace("H", "T",2)) # thay thế 2 lần H bằng T

#đảo chuỗi
print(str1[::-1]) #step -1 sẽ chạy ngược lại
print(''.join(reversed(str1))) # dùng câu lệnh reversed
my_string = "apple,banana,cherry"
my_list = my_string.split(",")  # Chuyển thành danh sách ["apple", "banana", "cherry"]
joined_string = ",".join(my_list)  # Chuyển thành chuỗi "apple,banana,cherry"

#format : chuyển về cùng kiểu chuỗi
age = 18
high = 130
txt = "hello {1} {0}"
print(txt.format(age, high))

# METHODS

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
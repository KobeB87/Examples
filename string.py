#coding:utf-8

str = "Hello world world !"
print(str)
print(str.replace("world", "planet earth"))

str = "elem1|elem2|elem3"
print(str.split("|"))

str = "12345678"
print("Chaine : {}".format(str))
print("12 is present : {}".format("12" in str))
print("isalpha : {}".format(str.isalpha()))
print("isalnum : {}".format(str.isalnum()))
print("isdigit : {}".format(str.isdigit()))
print("isdecimal : {}".format(str.isdecimal()))
print("islower : {}".format(str.islower()))
print("isupper : {}".format(str.isupper()))
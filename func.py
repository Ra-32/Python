# builtin function 
# print(),len(),sum()
# a= 10
# def greeting():
#     if a == 10:
#      return (a+a)
   

# def machine():
#     pass

# def color():
#     pass

# # car is object 
# #  greeting()
# # machine()
# # color()
# print(greeting())

#nested function function inside function
# def outer():
#     def inner():
#         return "inner function"
#     return "outer funtion"

# print(outer()) # only print outer function 

# def outer():
#     def inner():
#         return "inner function"
#     print(inner())
#     return "outer funtion"

# print(outer()) print both 
# list =[]

# def function_name(a,b,c):
#     if b == 10:
#         list.append(b)
#     return list

# a =3
# b=10
# c =9

# print(function_name(a,b,c))

# list =[]

# def function_name(a,b,c):
#     # if b == 10:
#     #     list.append(b)
#     #     print(list)
#     for  i in range(1,5):
#         print(i)
#         list.append(i)
        
#     return list

# a =3
# b=10
# c =9

# print(function_name(a,b,c))

# a = 10
# def my_function():
#     # a=+1


#     # a=10
#     global a
#     a+=1
#     return a
# print(a)

# print(my_function())


# def student(country="india"):
#     def change(country):
#         if country == "india":
#             return("usa")
#         elif country =="uk":
#             return("india")   
#         else:
#             return(country)
#     return (change(country))

# print(student("uk"))
# print(student("india"))
# print(student())
x="global"
def outer():
    global x
    x= "outer"
    def inner():
       # nonlocal x
        x ="inner"
    inner()
    print(x)
outer()
print(x)








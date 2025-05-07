
# Basic List in Python
a=[10,"sugash",20,30,"@",40.0]
print(type(a[1]))
print(a)
a.append(50)
a.insert(0,20)
b=[10,20,20]
a.extend(b)
print(a)
# list comprehension
a=[i*3 for i in range(10)]
print(a)
#using nested loop
a=[(i,j) for i in range(5) for j in range(5)]
print(a)
'''
a=[1,2,3,4,5]
print(a)
a[2]=67
print(a)

''

a=[1,2,3,4,5]
b=a
print(id(a))
print(id(b))

''

a=[1,2,3,4,5]
b=a
a[2]=0
print("a"+str(a))
print("b"+str(b))
''

a=[1,2,3,4]
b=a
a=a+[10,0]
print("a:"+str(a))
print("b:"+str(b))
''

a="1 2 3 4"
alist=a.split()
print(alist)

''

a="Python is a animal"
b=a.split('a')
print(b)
''
a="Python is a animal"
c=a.split("n")
print("n".join(c))
''

a=[1,2,3]
a.append(7)
print(a)

'''

a=[1,2,3,4]
a.extend([7,8,9])
a.sort()
print(a)


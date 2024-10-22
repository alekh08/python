#type of tuple
'''
t=(1,2,3,4,5,6)
print(type(t))


t=(1,2,3,4,5,6)
print(t[5]==6)


#length of tuple
t=(1,2,3,4,5,6)
print(len(t))

#iteration
t=(1,2,3,4,5,6)
for item in t:
    print(item)
''

i=0
t=(1,2,3,4,5,6)
while(i>0):
    print(t[i])

'''
#enumerate
t=(1,2,3,4,5,6)
for index in enumerate(t):
    print(index)
    
#nested tuple
t=((1,2,3),(3,6,7),(7,8,9))
for inner_t in t:
    print("inner tuple",inner_t)
    for item in inner_t:
        print(item)

t=(1,2,3)
print(-3,-1)

#tuple methods


l=(1,2,3,4)
print(l.index(2))


#min and max fuction
l=(10,20,30)
print(max(l))
print(min(l))

#sorting in tuple
l=(10,20,30,90,87,56,23,12)
print(sorted(l))
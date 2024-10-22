'''

for j in range(1,5):
    print("*"*j)
print("\n")

''

for a in range(0,6):
    print(' '*(6-a-1)+'*'*(a*2+1))
    
''
    
for i in range(6,0,-1):
    print('*'*(i-1))
    
    
''

ch=65

for a in range (1,6):
    l=""
    for i in range(a):
        l+=chr(ch)
        ch=ch+1
    print(l)
    
    
''
ch=65
l=""
for a in range(1,6):
    
    l+=chr(ch)
    ch=ch+1
    print(l)
    
''

for i in range(1,6):
    for j in range(1,6):
        print(j,end='')
    print()

#output:
12345
12345
12345
12345
12345

'''
for i in range(1,5):
    for j in range(1,5):
        
        




'''
#output:
                1
            1       2
        1       2       3
    1       2       3      4
    
'''
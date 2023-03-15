#for loop
#range function
#1 to 100
#odd number between 1 to 100
#even number between 1 to 100
n = 100
for i in range(n):
    if(i%2 == 0):
        print("even no:",i)
    else:
        print("odd no:",i)
for i in range(1,101,2):
    #range(start,end,step)
    print(i,end=' ')
print()    
for i in range(2,102,2):
    #range(start,end,step)
    print(i,end=' ')

#reverse order
for i in range(n,1,-1):
    print(i,end=" ")
#99 97...0

for i in range(99,0,-1):
    print(i,end=" ")


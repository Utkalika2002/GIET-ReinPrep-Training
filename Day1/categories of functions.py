#categories of functions
#based on arguments
#1:positional arguments
def function1(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function1(10,20,30,40)
function1(100,"200",300,400)

#2 keyword arguments
def function2(num1,num2,num3,num4):
    print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4=10,num1=20,num2=30,num3=40)
def function3(name,rollno,branch,collegename="GIET"):
    print(name,rollno,branch,collegename)
function3("Utk",289,"CSE")
function3("Ashu",281,"CST")

def function4(*var):
    for i in var:
        print(i,end='')
function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)

def add(*var):#tuple=
    sum1=0
    for i in var:#10,20
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30,40))
print(add(10,20,30,40,50,60))



#functions
def function1():
    print("sarangheyo")
function1()
def function2(num1,num2):
    print("num1=",num1,"num2=",num2)
    #print()_str_
function2(10,20)
def function3(num1,num2):
    num3=num1+num2
    return num3
print("value returned",function3(100,200))
def function4(num1,num2):
    num3=num1+num2
    return num3
print("value returned",function4(10,20.2))
def function5(num1,num2):
    num3=float(num1)+num2
    return num3
print("value returned",function5('10',20.2))


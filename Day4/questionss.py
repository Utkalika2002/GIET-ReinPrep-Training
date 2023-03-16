##q1 find the largest prime factor
import math
def prime(j):
    for k in range(2,int(math.sqrt(j))+1):
        if(j%k==0):
            return 0
    return j 
def prime_list(s):
    m=0
    for j in s:
        d=prime(j)
        if d!=0:
            m=max(m,d)
    return m
def Summ(i):
    s=[]
    for j in range(1,i+1):
        if(i%j==0):
            s.append(j)
    return prime_list(s)
n=int(input())
su=0
for i in range(n,n+9):
    su=su+Summ(i)
print("Sum",su)

##q2 nearest pallindrome which accepts the no & returns the nearest palindrome >given no
import sys
def next_smallest_palindrome(num):
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i 
print(next_smallest_palindrome(99))
print(next_smallest_palindrome(1221))

##q3 input of a list in which patient id & medicine type in present,we've to finf the max.
l = list(map(str,input().split(",")))
P = 0
E = 0
O = 0
for i in range(1,len(l),2):
    if(l[i] == 'P'):
        P +=1 
    elif(l[i] == 'O'):
        O +=1 
    elif(l[i] == 'E'):
        E +=1
if(P>O and P>E):
    print("Pediatrics")
elif(O>E and O>P):
    print("Orthoprdics")
elif(E>O and E>P):
    print("ENT")

##q4 display all the common characters between 2 strings.Return -1 if there is no matching characters
s1 = "I like Python"
s2 = "Java is a avery popular language"
s3 =''
for i in s1:
    if(i == " "):
        pass
    else:
        if(i in s2):
            if(i not in s3):
                s3 +=i 
print(s3)
##----------------------------------------------------------------------------------------------------
class Example:
    def __init__(self,num):
        self.num=num
        
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())

##--------------------------------------------------------------------------------------------------------------
class Customer:
    def __init__(self,id):
        self.id = 100
        
c1=Customer(200)
print(c1.id)

##-------------------------------------------------------------------------------------------------------------

class Book:
    def __init__(self):
        self.title=None
my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn Python the hard way"

my_fav.title="Learning Python"

print("My favourite is",my_fav.title)
print("Your's is",your_fav.title)

##------------------------------------------------------------------------------------------------------------------

class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material
s = Shoe(1000, "Canvas")
print("the unique id of the object",id(s))

##----------------------------------------------------------------------------------------------------------------------

class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material
    def __str__(self):
        return "Shoe price :"+str(self.price)+" and material :"+ str(self.material)
s = Shoe(1000, "Canvas")
print(s)

##--------------------------------------------------------------------------------------------------------------------

class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("displaying details")
    def purchase(self):
        print("calculating price")
Mobile().purchase()
Mobile().display()

##-----------------------------------------------------------------------------------------------------------------------

class Mobile:
    def __init__(self,brand,price):
        self.price = price
        self.brand = brand
        self.total_price = None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price=self.price-self.price*(discount/100)
        print("total price of",self.brand, "mobile is",self.total_price)
        
m1=Mobile("Apple",20000)
m2=Mobile("Samsung",10000)
m1.purchase()
m2.purchase()

##----------------------------------------------------------------------------------------------------------------------------

class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance ##private
    def update_balance(self,amount):
        if amount<1000 and amount>0:
            self.__wallet_balance += amount
    def show_balance(self):
        print("The balance is",self.__wallet_balance)
    def value(self):
        return self.__wallet_balance
        
c1=Customer(100,"Gopal",24,100)
c1.update_balance(500)
c1.show_balance()
print(c1.value())
#print(c1.__wallet_balance)

##------------------------------------------------------------------------------------------------------------------------------

class Dam:
    def __init__(self,name,length):
        self.name = name
        self.__length = length
    def get_length(self):
        return self.__length
dam1=Dam("ABC Dam",3.5)
print(dam1.name)
print(dam1.get_length())

##------------------------------------------------------------------------------------------------------------------------------------

class Table:
    def __init__(self):
        self.no_of_legs= 4
        self.__glass_top =None
        self.__wooden_top =None
        
    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify(self,glass_top,wooden_top):
        self.assign_data(glass_top,wooden_top)
        if(self.__wooden_top == True):
            rate = 30000
        elif(self.__glass_top == True):
            rate = 20000
        else:
            rate = 0 
        return rate
rate = Table().identify(True,False)
print(rate)

##-------------------------------------------------------------------------------------------------------------------------------------------



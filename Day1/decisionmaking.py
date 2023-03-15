#Decision making statements
#read a number-->
#multiple 3-->
#multiple 5-->
n = int(input())
if(n%3 == 0):
    print("Multiple of 3")
if(n%5 == 0):
    print("Multiple of 5")
elif(n%3 == 0 and n%5==0):
    print("Multiple of 3 and 5")
else:
    print("Invalid")
